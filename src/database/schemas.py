from pydantic import BaseModel
from typing import Optional

class GameBase(BaseModel):
    name: str
    alternative_names: Optional[list] = None
    artworks: Optional[list] = None
    category: Optional[int] = None
    cover: Optional[int] = None
    cover_url: Optional[str] = None
    created_at: Optional[int] = None
    final_release_date: Optional[str] = None
    franchises: Optional[list] = None
    game_modes: Optional[list] = None
    involves_companies: Optional[str] = None
    parent_game: Optional[str] = None
    platforms: Optional[list] = None
    player_perspectives: Optional[list] = None
    release_dates: Optional[list] = None
    screenshots: Optional[list] = None
    similar_games: Optional[list] = None
    slug: Optional[str] = None
    summary: Optional[str] = None
    tags: Optional[list] = None
    themes: Optional[list] = None
    updated_at: Optional[int] = None
    url: Optional[str] = None
    websites: Optional[list] = None
    checksum: Optional[str] = None
    collections: Optional[list] = None
    message: Optional[str] = None

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
