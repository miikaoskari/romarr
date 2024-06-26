import os
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext

from sqlalchemy.orm import Session

from .database import crud, models, schemas
from .database.helper import create_schema_instances
from .database.database import SessionLocal, engine

from .filesystem.imagecache import ImageCache

from .igdb import Igdb

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

# Security
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


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


# Login
@app.post("/api/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=form_data.username)
    if db_user is None:
        raise HTTPException(status_code=400, detail="Incorrect username")

    # TODO: verify password


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

            image_cache = ImageCache("cache")

            cover_id = game_data.get("cover", None)
            if cover_id:
                cover_url = igdb.get_game_cover(cover_id)
                print(cover_url)
                game_data["cover_path"] = image_cache.get_image(cover_url[0]["url"], "cover_big")

            # Fetch and save artworks
            artwork_ids = game_data.pop("artworks", [])
            artworks = []
            for artwork_id in artwork_ids:
                artwork_url = igdb.get_game_artwork(artwork_id)
                artwork_path = image_cache.get_image(artwork_url[0]["url"], "artwork_big")
                artworks.append(schemas.ArtworkCreate(artwork=artwork_id, artwork_path=artwork_path))

            # Fetch and save screenshots
            screenshot_ids = game_data.pop("screenshots", [])
            screenshots = []
            for screenshot_id in screenshot_ids:
                screenshot_url = igdb.get_game_screenshots(screenshot_id)
                screenshot_path = image_cache.get_image(screenshot_url[0]["url"], "screenshot_big")
                screenshots.append(schemas.ScreenshotCreate(screenshot=screenshot_id, screenshot_path=screenshot_path))

            dlcs = create_schema_instances(game_data.pop("dlcs", []), schemas.DLC, 'dlc')
            expansions = create_schema_instances(game_data.pop("expansions", []), schemas.Expansion, 'expansion')
            franchises = create_schema_instances(game_data.pop("franchises", []), schemas.Franchise, 'franchise')
            genres = create_schema_instances(game_data.pop("genres", []), schemas.Genre, 'genre')
            platforms = create_schema_instances(game_data.pop("platforms", []), schemas.Platform, 'platform')
            release_dates = create_schema_instances(game_data.pop("release_dates", []), schemas.ReleaseDate,
                                                    'release_date')

            game = schemas.GameCreate(
                **game_data,
                artworks=artworks,
                dlcs=dlcs,
                expansions=expansions,
                franchises=franchises,
                genres=genres,
                platforms=platforms,
                release_dates=release_dates,
                screenshots=screenshots
            )
            return crud.create_game(db=db, game=game)
        else:
            raise ValueError("Unexpected game data format from IGDB API")
    else:
        raise HTTPException(status_code=404, detail="Game not found in IGDB")


# Add indexer to database
@app.post("/api/indexers/", response_model=schemas.Indexer)
def create_indexer(indexer: schemas.IndexerCreate, db: Session = Depends(get_db)):
    db_indexer = crud.get_indexer_by_name(db, name=indexer.name)
    if db_indexer:
        raise HTTPException(status_code=400, detail="Indexer already registered")
    return crud.create_indexer(db=db, indexer=indexer)


# Add client to database
@app.post("/api/clients/", response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    db_client = crud.get_client_by_name(db, name=client.name)
    if db_client:
        raise HTTPException(status_code=400, detail="Client already registered")
    return crud.create_client(db=db, client=client)


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
    igdb_query = Igdb()
    igdb_query.get_config()
    return igdb_query.get_games_by_name(query)


# Get all games from database
@app.get("/api/games/all", response_model=list[schemas.Game])
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


# Serve the images
if not os.path.exists("cache"):
    os.makedirs("cache")
app.mount("/cache", StaticFiles(directory="cache", html=False), name="images")

# Serve the frontend
app.mount("/", StaticFiles(directory="frontend/build", html=True), name="frontend")


@app.get("/{catch_all:path}")
async def serve_frontend(catch_all: str):
    if os.path.exists(f"frontend/build/{catch_all}"):
        return FileResponse(f"frontend/build/{catch_all}")
    else:
        return FileResponse("frontend/build/index.html")
