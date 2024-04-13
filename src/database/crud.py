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
    artworks = [models.Artwork(**artwork.model_dump()) for artwork in game.artworks]
    dlcs = [models.DLC(**dlc.model_dump()) for dlc in game.dlcs]
    expansions = [models.Expansion(**expansion.model_dump()) for expansion in game.expansions]
    franchises = [models.Franchise(**franchise.model_dump()) for franchise in game.franchises]
    genres = [models.Genre(**genre.model_dump()) for genre in game.genres]
    platforms = [models.Platform(**platform.model_dump()) for platform in game.platforms]
    release_dates = [models.ReleaseDate(**release_date.model_dump()) for release_date in game.release_dates]
    screenshots = [models.Screenshot(**screenshot.model_dump()) for screenshot in game.screenshots]

    db_game = models.Game(
        name=game.name,
        artworks=artworks,
        cover=game.cover,
        dlcs=dlcs,
        expansions=expansions,
        franchises=franchises,
        genres=genres,
        platforms=platforms,
        rating=game.rating,
        release_dates=release_dates,
        screenshots=screenshots,
        summary=game.summary,
        url=game.url,
        checksum=game.checksum,
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
