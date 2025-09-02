import json
from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Session, select

from db import Game, get_session, create_db_and_tables
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

@app.get("/api/igdb")
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
    
@app.get("/api/games")
async def read_games(session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    """Read all games from database
    """
    try:
        return session.exec(select(Game).offset(offset).limit(limit)).all()
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/api/games/{igdb_id}")
async def add_game(igdb_id: int, session: SessionDep):
    """Query IGDB for game and add to database.
    """
    try:
        existing = session.exec(select(Game).where(Game.igdb_id == igdb_id)).first()
        if existing:
            return existing

        igdb_data = igdb_api.get_game(igdb_id)[0]

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
    
@app.delete("/api/games/{igdb_id}")
async def delete_game(igdb_id: int, session: SessionDep):
    """Delete game from database
    """
    pass
