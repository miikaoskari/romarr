import os

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from .database import crud, models, schemas
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

            # Extract data for alternative names and create instances
            alternative_names_data = game_data.pop("alternative_names", None)
            alternative_names = []
            if alternative_names_data:
                for name_id in alternative_names_data:
                    alternative_names.append(schemas.AlternativeName(alternative_name=name_id))
            artworks_data = game_data.pop("artworks", None)
            artworks = []
            if artworks_data:
                for artwork_id in artworks_data:
                    artworks.append(schemas.Artwork(artwork=artwork_id))
            franchises_data = game_data.pop("franchises", None)
            franchises = []
            if franchises_data:
                for franchise_id in franchises_data:
                    franchises.append(schemas.Franchise(franchise=franchise_id))
            game_modes_data = game_data.pop("game_modes", None)
            game_modes = []
            if game_modes_data:
                for game_mode_id in game_modes_data:
                    game_modes.append(schemas.GameMode(game_mode=game_mode_id))
            involved_companies_data = game_data.pop("involved_companies", None)
            involved_companies = []
            if involved_companies_data:
                for involved_company_id in involved_companies_data:
                    involved_companies.append(schemas.InvolvedCompany(involved_company=involved_company_id))
            platforms_data = game_data.pop("platforms", None)
            platforms = []
            if platforms_data:
                for platform_id in platforms_data:
                    platforms.append(schemas.Platform(platform=platform_id))
            player_perspectives_data = game_data.pop("player_perspectives", None)
            player_perspectives = []
            if player_perspectives_data:
                for player_perspective_id in player_perspectives_data:
                    player_perspectives.append(schemas.PlayerPerspective(player_perspective=player_perspective_id))
            release_dates_data = game_data.pop("release_dates", None)
            release_dates = []
            if release_dates_data:
                for release_date_id in release_dates_data:
                    release_dates.append(schemas.ReleaseDate(release_date=release_date_id))
            screenshots_data = game_data.pop("screenshots", None)
            screenshots = []
            if screenshots_data:
                for screenshot_id in screenshots_data:
                    screenshots.append(schemas.Screenshot(screenshot=screenshot_id))
            similar_games_data = game_data.pop("similar_games", None)
            similar_games = []
            if similar_games_data:
                for similar_game_id in similar_games_data:
                    similar_games.append(schemas.SimilarGame(similar_game=similar_game_id))
            tags_data = game_data.pop("tags", None)
            tags = []
            if tags_data:
                for tag_id in tags_data:
                    tags.append(schemas.Tag(tag=tag_id))
            themes_data = game_data.pop("themes", None)
            themes = []
            if themes_data:
                for theme_id in themes_data:
                    themes.append(schemas.Theme(theme=theme_id))
            websites_data = game_data.pop("websites", None)
            websites = []
            if websites_data:
                for website_id in websites_data:
                    websites.append(schemas.Website(website=website_id))
            collections_data = game_data.pop("collections", None)
            collections = []
            if collections_data:
                for collection_id in collections_data:
                    collections.append(schemas.Collection(collection=collection_id))

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
