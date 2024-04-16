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
        cover_path=game.cover_path,
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


def create_indexer(db: Session, indexer: schemas.IndexerCreate):
    db_indexer = models.Indexer(name=indexer.name, url=indexer.url, api_key=indexer.api_key, enabled=indexer.enabled)
    db.add(db_indexer)
    db.commit()
    db.refresh(db_indexer)
    return db_indexer


def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Client(name=client.name, url=client.url, client_id=client.client_id,
                              client_secret=client.client_secret, enabled=client.enabled)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


# READ
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_games(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Game).offset(skip).limit(limit).all()


def get_game_by_id(db: Session, game_id: int):
    return db.query(models.Game).filter(models.Game.id == game_id).first()


def get_indexer_by_name(db: Session, name: str):
    return db.query(models.Indexer).filter(models.Indexer.name == name).first()


def get_client_by_name(db: Session, name: str):
    return db.query(models.Client).filter(models.Client.name == name).first()


# UPDATE


# DELETE
