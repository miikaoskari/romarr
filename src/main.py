from fastapi import FastAPI
from .igdb import Igdb, Game

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello"}


@app.get("/games/{game_id}")
async def get_game(game_id):
    return {"game_id": game_id}


@app.get("/search/{query}")
async def search(query):
    igdb_query = Igdb(query)
    igdb_query.get_config()
    igdb_query.search_game()
    return {"query": igdb_query.games}


@app.get("/games")
async def get_games():
    return {"games": "games"}
