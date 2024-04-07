from sqlalchemy.orm import Session
from hashlib import pbkdf2_hmac

from . import models, schemas
from os import urandom


# CREATE
def create_user(db: Session, user: schemas.UserCreate):
    iters = 500_000
    salt = urandom(32)
    dk = pbkdf2_hmac("sha256", user.hashed_password.encode("utf-8"), salt, iters)
    hashed_password = dk.hex()
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_game(db: Session, game: schemas.GameCreate):
    alternative_names = [models.AlternativeName(**alternative_name.model_dump()) for alternative_name in game.alternative_names]
    artworks = [models.Artwork(**artwork.model_dump()) for artwork in game.artworks]
    franchises = [models.Franchise(**franchise.model_dump()) for franchise in game.franchises]
    game_modes = [models.GameMode(**game_mode.model_dump()) for game_mode in game.game_modes]
    involved_companies = [models.InvolvedCompany(**involved_company.model_dump()) for involved_company in game.involved_companies]
    platforms = [models.Platform(**platform.model_dump()) for platform in game.platforms]
    player_perspectives = [models.PlayerPerspective(**player_perspective.model_dump()) for player_perspective in game.player_perspectives]
    release_dates = [models.ReleaseDate(**release_date.model_dump()) for release_date in game.release_dates]
    screenshots = [models.Screenshot(**screenshot.model_dump()) for screenshot in game.screenshots]
    similar_games = [models.SimilarGame(**similar_game.model_dump()) for similar_game in game.similar_games]
    tags = [models.Tag(**tag.model_dump()) for tag in game.tags]
    themes = [models.Theme(**theme.model_dump()) for theme in game.themes]
    websites = [models.Website(**website.model_dump()) for website in game.websites]
    collections = [models.Collection(**collection.model_dump()) for collection in game.collections]

    db_game = models.Game(
        name=game.name,
        alternative_names=alternative_names,
        artworks=artworks,
        category=game.category,
        cover=game.cover,
        created_at=game.created_at,
        final_release_date=game.final_release_date,
        franchises=franchises,
        game_modes=game_modes,
        involved_companies=involved_companies,
        parent_game=game.parent_game,
        platforms=platforms,
        player_perspectives=player_perspectives,
        release_dates=release_dates,
        screenshots=screenshots,
        similar_games=similar_games,
        slug=game.slug,
        summary=game.summary,
        tags=tags,
        themes=themes,
        updated_at=game.updated_at,
        url=game.url,
        websites=websites,
        checksum=game.checksum,
        collections=collections,
        message=game.message
    )
    print(db_game)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


# READ
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_games(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Game).offset(skip).limit(limit).all()


def get_game_by_id(db: Session, game_id: int):
    return db.query(models.Game).filter(models.Game.id == game_id).first()

# UPDATE


# DELETE
