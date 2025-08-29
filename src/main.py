import json
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Session

from db import get_session
from igdb_api import IGDBApi


def read_token() -> dict:
    with open("token_response.json", "r") as f:
        return json.loads(f.read())
    
token = read_token()

app = FastAPI()

igdb_api = IGDBApi(token)

SessionDep = Annotated[Session, Depends(get_session)]

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
async def read_games(session: SessionDep):
    """Read all games from database
    """
    try:
        return 
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/api/games/{igdb_id}")
async def add_game(igdb_id: int, session: SessionDep):
    """Query IGDB for game and add to database.
    """
    try:
        return igdb_api.get_game(igdb_id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.delete("/api/games/{igdb_id}")
async def delete_game(igdb_id: int, session: SessionDep):
    """Delete game from database
    """
    pass
