import os

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from database import crud, models, schemas
from database.database import SessionLocal, engine

from igdb import Igdb

models.Base.metadata.create_all(bind=engine)

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

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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

# Create user
@app.post("/api/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="username already registered")

# Get user by id
@app.get("/api/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Function for searching for games through IGDB
@app.get("/api/search/{query}")
async def search(query):
    igdb_query = Igdb(query)
    igdb_query.get_config()
    igdb_query.search_game()
    return {"query": [game.get_small_description() for game in igdb_query.games]}

# Get all games from database
@app.get("/api/games", response_model=list[schemas.Game])
def read_games(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    games = crud.get_games(db, skip=skip, limit=limit)
    return games

# Get game from database by id
@app.get("/api/games/{game_id}", response_model=schemas.Game)
def read_game(game_id: int, db: Session = Depends(get_db)):
    game = crud.get_game_by_id(db, game_id=game_id)
    if game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    return game

