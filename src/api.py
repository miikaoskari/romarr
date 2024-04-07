import os

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from .database import crud, models, schemas
from .database.helper import create_schema_instances
from .database.database import SessionLocal, engine

from .igdb import Igdb
from .game import Game

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
app.mount("/static", StaticFiles(directory="frontend/build", html=True), name="frontend")


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
    if len(user.hashed_password) > 1024:
        raise HTTPException(status_code=400, detail="password too long. maximum length 1024")
    return crud.create_user(db=db, user=user)


# Add game to database
@app.post("/api/games/add", response_model=schemas.Game)
def create_game(game_id: int, db: Session = Depends(get_db)):
    igdb = Igdb()
    igdb.get_config()
    game_data = igdb.get_game_by_id(game_id)

    db_game = db.query(models.Game).filter(models.Game.id == game_id).first()
    if db_game:
        raise HTTPException(status_code=400, detail="Game already in library")

    if game_data:
        if isinstance(game_data, list) and len(game_data) == 1:  # Check if it's a list with one item
            game_data = game_data[0]  # Extract the dictionary from the list

            alternative_names = create_schema_instances(game_data.pop("alternative_names"), schemas.AlternativeName, 'alternative_name')
            artworks = create_schema_instances(game_data.pop("artworks"), schemas.Artwork, 'artwork')
            franchises = create_schema_instances(game_data.pop("franchises"), schemas.Franchise, 'franchise')
            game_modes = create_schema_instances(game_data.pop("game_modes"), schemas.GameMode, 'game_mode')
            involved_companies = create_schema_instances(game_data.pop("involved_companies"), schemas.InvolvedCompany, 'involved_company')
            platforms = create_schema_instances(game_data.pop("platforms"), schemas.Platform, 'platform')
            player_perspectives = create_schema_instances(game_data.pop("player_perspectives"), schemas.PlayerPerspective, 'player_perspective')
            release_dates = create_schema_instances(game_data.pop("release_dates"), schemas.ReleaseDate, 'release_date')
            screenshots = create_schema_instances(game_data.pop("screenshots"), schemas.Screenshot, 'screenshot')
            similar_games = create_schema_instances(game_data.pop("similar_games"), schemas.SimilarGame, 'similar_game')
            tags = create_schema_instances(game_data.pop("tags"), schemas.Tag, 'tag')
            themes = create_schema_instances(game_data.pop("themes"), schemas.Theme, 'theme')
            websites = create_schema_instances(game_data.pop("websites"), schemas.Website, 'website')
            collections = create_schema_instances(game_data.pop("collections"), schemas.Collection, 'collection')

            game = schemas.GameCreate(
                **game_data,
                alternative_names=alternative_names,
                artworks=artworks,
                franchises=franchises,
                game_modes=game_modes,
                involved_companies=involved_companies,
                platforms=platforms,
                player_perspectives=player_perspectives,
                release_dates=release_dates,
                screenshots=screenshots,
                similar_games=similar_games,
                tags=tags,
                themes=themes,
                websites=websites,
                collections=collections
            )
            return crud.create_game(db=db, game=game)
        else:
            raise ValueError("Unexpected game data format from IGDB API")
    else:
        raise HTTPException(status_code=404, detail="Game not found in IGDB")


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
