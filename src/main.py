import json
from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Session, select
from torznab import Torznab

from db import Game, Indexer, get_session, create_db_and_tables, IndexerCreate, IndexerPublic
from igdb_api import IGDBApi


def read_token() -> dict:
    with open("token_response.json", "r") as f:
        return json.loads(f.read())
    
token = read_token()
igdb_api = IGDBApi(token)

SessionDep = Annotated[Session, Depends(get_session)]

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/api/igdb", tags=["games"])
async def search_games(search: str, limit: int = 20):
    """Query IGDB for games and return JSON results.

    Runs a search for given parameter
    """
    try:
        return igdb_api.search_games(search, limit)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/api/games", tags=["games"])
async def read_games(session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    """Read all games from database
    """
    try:
        return session.exec(select(Game).offset(offset).limit(limit)).all()
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/api/games/{igdb_id}", tags=["games"])
async def add_game(igdb_id: int, session: SessionDep):
    """Add a new game by given igdb id
    """
    try:
        existing = session.exec(select(Game).where(Game.igdb_id == igdb_id)).first()
        if existing:
            return existing

        igdb_data = igdb_api.get_game(igdb_id)

        game = Game(
            igdb_id=igdb_data['id'],
            cover_url=igdb_data['cover']['url'],
            name=igdb_data['name']
        )

        session.add(game)
        session.commit()
        session.refresh(game)
        return game
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.delete("/api/games/{igdb_id}", tags=["games"])
async def delete_game(igdb_id: int, session: SessionDep):
    """Delete game from database by igdb id
    """
    try:
        existing_game = session.exec(select(Game).where(Game.igdb_id == igdb_id)).first()

        if not existing_game:
            raise HTTPException(status_code=404, detail="Game not found")

        session.delete(existing_game)
        session.commit()
        return {"ok": True}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/games/{igdb_id}/indexers/results", tags=["games"])
async def find_results_from_indexers(igdb_id: int, session: SessionDep):
    try:
        indexers = session.exec(select(Indexer))
        game = session.exec(select(Game).where(Game.igdb_id == igdb_id)).first()

        if not game:
            raise HTTPException(status_code=404, detail="Game not found")

        for indexer in indexers:
            if indexer.api_key:
                tn = Torznab(indexer.api_key)
                tn.search_torrent(game.name, indexer.url)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/indexers", tags=["indexers"], response_model=IndexerPublic)
async def add_indexer(indexer: IndexerCreate, session: SessionDep):
    try:
        db_indexer = Indexer.model_validate(indexer)
        session.add(db_indexer)
        session.commit()
        session.refresh(db_indexer)
        return db_indexer
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.delete("/api/indexers/{indexer_id}", tags=["indexers"])
async def delete_indexer(indexer_id: int, session: SessionDep):
    indexer = session.get(Indexer, indexer_id)
    if not indexer:
        raise HTTPException(status_code=404, detail="Indexer not found")
    session.delete(indexer)
    session.commit()
    return {"ok": True}
