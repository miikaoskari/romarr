from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship, Mapped

from typing import List

from .database import Base


class Game(Base):
    __tablename__ = 'games'

    id: Mapped[int] = Column(Integer, primary_key=True)
    artworks: Mapped[List["Artwork"]] = relationship("Artwork", back_populates="game")
    cover = Column(String)
    dlcs: Mapped[List["DLC"]] = relationship("DLC", back_populates="game")
    expansions: Mapped[List["Expansion"]] = relationship("Expansion", back_populates="game")
    franchises: Mapped[List["Franchise"]] = relationship("Franchise", back_populates="game")
    genres: Mapped[List["Genre"]] = relationship("Genre", back_populates="game")
    name = Column(String)
    platforms: Mapped[List["Platform"]] = relationship("Platform", back_populates="game")
    rating = Column(Float)
    release_dates: Mapped[List["ReleaseDate"]] = relationship("ReleaseDate", back_populates="game")
    screenshots: Mapped[List["Screenshot"]] = relationship("Screenshot", back_populates="game")
    summary = Column(String)
    url = Column(String)
    checksum = Column(String)


class Artwork(Base):
    __tablename__ = 'artworks'

    id: Mapped[int] = Column(Integer, primary_key=True)
    artwork = Column(Integer)
    parent_id: Mapped[int] = Column(Integer, ForeignKey("games.id"))
    game: Mapped[Game] = relationship("Game", back_populates="artworks")

class DLC(Base):
    __tablename__ = 'dlcs'

    id: Mapped[int] = Column(Integer, primary_key=True)
    dlc = Column(Integer)
    parent_id: Mapped[int] = Column(Integer, ForeignKey("games.id"))
    game: Mapped[Game] = relationship("Game", back_populates="dlcs")

class Expansion(Base):
    __tablename__ = 'expansions'

    id: Mapped[int] = Column(Integer, primary_key=True)
    expansion = Column(Integer)
    parent_id: Mapped[int] = Column(Integer, ForeignKey("games.id"))
    game: Mapped[Game] = relationship("Game", back_populates="expansions")

class Franchise(Base):
    __tablename__ = 'franchises'

    id: Mapped[int] = Column(Integer, primary_key=True)
    franchise = Column(Integer)
    parent_id: Mapped[int] = Column(Integer, ForeignKey("games.id"))
    game: Mapped[Game] = relationship("Game", back_populates="franchises")

class Genre(Base):
    __tablename__ = 'genres'

    id: Mapped[int] = Column(Integer, primary_key=True)
    genre = Column(Integer)
    parent_id: Mapped[int] = Column(Integer, ForeignKey("games.id"))
    game: Mapped[Game] = relationship("Game", back_populates="genres")


class Platform(Base):
    __tablename__ = 'platforms'

    id: Mapped[int] = Column(Integer, primary_key=True)
    platform = Column(Integer)
    parent_id: Mapped[int] = Column(Integer, ForeignKey("games.id"))
    game: Mapped[Game] = relationship("Game", back_populates="platforms")


class ReleaseDate(Base):
    __tablename__ = 'release_dates'

    id: Mapped[int] = Column(Integer, primary_key=True)
    release_date = Column(Integer)
    parent_id: Mapped[int] = Column(Integer, ForeignKey("games.id"))
    game: Mapped[Game] = relationship("Game", back_populates="release_dates")


class Screenshot(Base):
    __tablename__ = 'screenshots'

    id: Mapped[int] = Column(Integer, primary_key=True)
    screenshot = Column(Integer)
    parent_id: Mapped[int] = Column(Integer, ForeignKey("games.id"))
    game: Mapped[Game] = relationship("Game", back_populates="screenshots")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
