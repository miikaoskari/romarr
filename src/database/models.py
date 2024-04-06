from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import MappedAsDataclass, mapped_column, relationship, Mapped

from typing import List

from .database import Base


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    alternative_names = relationship("AlternativeName", back_populates="parent")
    artworks = relationship("Artwork", back_populates="parent")
    category = Column(String)
    cover = Column(String)
    cover_url = relationship("CoverURL", back_populates="parent")
    created_at = Column(String)
    final_release_date = Column(String)
    franchises = relationship("Franchise", back_populates="parent")
    game_modes = relationship("GameMode", back_populates="parent")
    involved_companies = relationship("InvolvedCompany", back_populates="parent")
    parent_game = Column(String)
    platforms = relationship("Platform", back_populates="parent")
    player_perspectives = relationship("PlayerPerspective", back_populates="parent")
    release_dates = relationship("ReleaseDate", back_populates="parent")
    screenshots = relationship("Screenshot", back_populates="parent")
    similar_games = relationship("SimilarGame", back_populates="parent")
    slug = Column(String)
    summary = Column(String)
    tags = relationship("Tag", back_populates="parent")
    themes = relationship("Theme", back_populates="parent")
    updated_at = Column(String)
    url = Column(String)
    websites = relationship("Website", back_populates="parent")
    checksum = Column(String)
    collections = relationship("Collection", back_populates="parent")
    message = Column(String)


class AlternativeName(Base):
    __tablename__ = 'alt_names'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey("games.id"))
    parent = relationship("Game", back_populates="alternative_names")


class Artwork(Base):
    __tablename__ = 'artworks'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey("games.id"))
    parent = relationship("Game", back_populates="artworks")


class CoverURL(Base):
    __tablename__ = 'cover_urls'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey("games.id"))
    parent = relationship("Game", back_populates="cover_url")


class Franchise(Base):
    __tablename__ = 'franchises'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey("games.id"))
    parent = relationship("Game", back_populates="franchises")


class GameMode(Base):
    __tablename__ = 'game_modes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey("games.id"))
    parent = relationship("Game", back_populates="game_modes")


class InvolvedCompany(Base):
    __tablename__ = 'involved_companies'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey("games.id"))
    parent = relationship("Game", back_populates="involved_companies")


class Platform(Base):
    __tablename__ = 'platforms'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey("games.id"))
    parent = relationship("Game", back_populates="platforms")


class PlayerPerspective(Base):
    __tablename__ = 'player_perspectives'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey("games.id"))
    parent = relationship("Game", back_populates="player_perspectives")


class ReleaseDate(Base):
    __tablename__ = 'release_dates'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey("games.id"))
    parent = relationship("Game", back_populates="release_dates")


class Screenshot(Base):
    __tablename__ = 'screenshots'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey("games.id"))
    parent = relationship("Game", back_populates="screenshots")


class SimilarGame(Base):
    __tablename__ = 'similar_games'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey("games.id"))
    parent = relationship("Game", back_populates="similar_games")


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey("games.id"))
    parent = relationship("Game", back_populates="tags")


class Theme(Base):
    __tablename__ = 'themes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey("games.id"))
    parent = relationship("Game", back_populates="themes")


class Website(Base):
    __tablename__ = 'websites'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey("games.id"))
    parent = relationship("Game", back_populates="websites")


class Collection(Base):
    __tablename__ = 'collections'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey("games.id"))
    parent = relationship("Game", back_populates="collections")


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
