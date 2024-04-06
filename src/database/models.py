from sqlalchemy import Column, DateTime, Integer, String, Boolean
from sqlalchemy.orm import relationship

from .database import Base


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    alternative_names = Column(String)
    artworks = Column(String)
    category = Column(String)
    cover = Column(String)
    cover_url = Column(String)
    created_at = Column(String)
    final_release_date = Column(String)
    franchises = Column(String)
    game_modes = Column(String)
    involves_companies = Column(String)
    parent_game = Column(String)
    platforms = Column(String)
    player_perspectives = Column(String)
    release_dates = Column(String)
    screenshots = Column(String)
    similar_games = Column(String)
    slug = Column(String)
    summary = Column(String)
    tags = Column(String)
    themes = Column(String)
    updated_at = Column(String)
    url = Column(String)
    websites = Column(String)
    checksum = Column(String)
    collections = Column(String)
    message = Column(String)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

