from pydantic import BaseModel
from typing import Optional, List


class AlternativeName(BaseModel):
    alternative_name: int


class Artwork(BaseModel):
    artwork: int


class Franchise(BaseModel):
    franchise: int


class GameMode(BaseModel):
    game_mode: int


class PlayerPerspective(BaseModel):
    player_perspective: int


class InvolvedCompany(BaseModel):
    involved_company: int


class Platform(BaseModel):
    platform: int


class ReleaseDate(BaseModel):
    release_date: int


class Screenshot(BaseModel):
    screenshot: int


class SimilarGame(BaseModel):
    similar_game: int


class Tag(BaseModel):
    tag: int


class Theme(BaseModel):
    theme: int


class Website(BaseModel):
    website: int


class Collection(BaseModel):
    collection: int


class GameBase(BaseModel):
    name: str
    alternative_names: Optional[List[AlternativeName]] = None
    artworks: Optional[List[Artwork]] = None
    category: Optional[int] = None
    cover: Optional[int] = None
    created_at: Optional[int] = None
    final_release_date: Optional[str] = None
    franchises: Optional[List[Franchise]] = None
    game_modes: Optional[List[GameMode]] = None
    involved_companies: Optional[List[InvolvedCompany]] = None
    parent_game: Optional[str] = None
    platforms: Optional[List[Platform]] = None
    player_perspectives: Optional[List[PlayerPerspective]] = None
    release_dates: Optional[List[ReleaseDate]] = None
    screenshots: Optional[List[Screenshot]] = None
    similar_games: Optional[List[SimilarGame]] = None
    slug: Optional[str] = None
    summary: Optional[str] = None
    tags: Optional[List[Tag]] = None
    themes: Optional[List[Theme]] = None
    updated_at: Optional[int] = None
    url: Optional[str] = None
    websites: Optional[List[Website]] = None
    checksum: Optional[str] = None
    collections: Optional[List[Collection]] = None
    message: Optional[str] = None


class GameCreate(GameBase):
    pass


class Game(GameBase):
    id: int

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    hashed_password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True
