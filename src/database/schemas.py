from pydantic import BaseModel
from typing import Optional, List


class AlternativeName(BaseModel):
    id: int
    alternative_name: int
    parent_id: int


class Artwork(BaseModel):
    id: int
    artwork: int
    parent_id: int


class CoverURL(BaseModel):
    id: int
    cover_url: int
    parent_id: int


class Franchise(BaseModel):
    id: int
    franchise: int
    parent_id: int


class GameMode(BaseModel):
    id: int
    game_mode: int
    parent_id: int


class PlayerPerspective(BaseModel):
    id: int
    player_perspective: int
    parent_id: int


class InvolvedCompany(BaseModel):
    id: int
    involved_company: int
    parent_id: int


class Platform(BaseModel):
    id: int
    platform: int
    parent_id: int


class ReleaseDate(BaseModel):
    id: int
    release_date: int
    parent_id: int


class Screenshot(BaseModel):
    id: int
    screenshot: int
    parent_id: int


class SimilarGame(BaseModel):
    id: int
    similar_game: int
    parent_id: int


class Tag(BaseModel):
    id: int
    tag: int
    parent_id: int


class Theme(BaseModel):
    id: int
    theme: int
    parent_id: int


class Website(BaseModel):
    id: int
    website: int
    parent_id: int


class Collection(BaseModel):
    id: int
    collection: int
    parent_id: int


class GameBase(BaseModel):
    name: str
    alternative_names: Optional[List[AlternativeName]] = None
    artworks: Optional[List[Artwork]] = None
    category: Optional[int] = None
    cover: Optional[int] = None
    cover_url: Optional[List[CoverURL]] = None
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
