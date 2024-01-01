from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .igdb import Igdb, Game

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    return {"query": [game.get_small_description() for game in igdb_query.games]}

@app.get("/games")
async def get_games():
    return {"games": "games"}
