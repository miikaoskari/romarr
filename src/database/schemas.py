from pydantic import BaseModel
from typing import Optional

class GameBase(BaseModel):
    name: str
    alternative_names: Optional[str] = None
    artworks: Optional[str] = None
    category: Optional[str] = None
    cover: Optional[str] = None
    cover_url: Optional[str] = None
    created_at: Optional[str] = None
    final_release_date: Optional[str] = None
    franchises: Optional[str] = None
    game_modes: Optional[str] = None
    involves_companies: Optional[str] = None
    parent_game: Optional[str] = None
    platforms: Optional[str] = None
    player_perspectives: Optional[str] = None
    release_dates: Optional[str] = None
    screenshots: Optional[str] = None
    similar_games: Optional[str] = None
    slug: Optional[str] = None
    summary: Optional[str] = None
    tags: Optional[str] = None
    themes: Optional[str] = None
    updated_at: Optional[str] = None
    url: Optional[str] = None
    websites: Optional[str] = None
    checksum: Optional[str] = None
    collections: Optional[str] = None

class GameCreate(GameBase):
    pass

class Game(GameBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    hashed_password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
