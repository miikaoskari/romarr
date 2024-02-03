import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from .igdb import Igdb

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


# Serve the API
@app.get("/api")
async def read_api():
    return {"message": "hello"}


# Serve the frontend
app.mount("/", StaticFiles(directory="frontend/build", html=True), name="frontend")


@app.get("/{catch_all:path}")
async def serve_frontend(catch_all: str):
    if os.path.exists(f"frontend/build/{catch_all}"):
        return FileResponse(f"frontend/build/{catch_all}")
    else:
        return FileResponse("frontend/build/index.html")


# Function for getting a game by ID
@app.get("/api/games/{game_id}")
async def get_game(game_id):
    return {"game_id": game_id}


# Function for searching for games
@app.get("/api/search/{query}")
async def search(query):
    igdb_query = Igdb(query)
    igdb_query.get_config()
    igdb_query.search_game()
    return {"query": [game.get_small_description() for game in igdb_query.games]}


# Function for getting all games
@app.get("/api/games")
async def get_games():
    return {"games": "games"}


# Function for adding a game
@app.post("/api/games")
async def add_game():
    return {"game": "game"}


# Function for deleting a game
@app.delete("/api/games/{game_id}")
async def delete_game(game_id):
    return {"game_id": game_id}

