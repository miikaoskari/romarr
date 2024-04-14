from pydantic import BaseModel
from typing import Optional, List


class Artwork(BaseModel):
    artwork: int
    artwork_path: str


class ArtworkCreate(Artwork):
    pass


class DLC(BaseModel):
    dlc: int


class Expansion(BaseModel):
    expansion: int


class Franchise(BaseModel):
    franchise: int


class Genre(BaseModel):
    genre: int


class Platform(BaseModel):
    platform: int


class ReleaseDate(BaseModel):
    release_date: int


class Screenshot(BaseModel):
    screenshot: int
    screenshot_path: str


class ScreenshotCreate(Screenshot):
    pass


class GameBase(BaseModel):
    name: str
    artworks: Optional[List[Artwork]] = None
    cover: Optional[int] = None
    cover_path: Optional[str] = None
    dlcs: Optional[List[DLC]] = None
    expansions: Optional[List[Expansion]] = None
    franchises: Optional[List[Franchise]] = None
    genres: Optional[List[Genre]] = None
    platforms: Optional[List[Platform]] = None
    rating: Optional[float] = None
    release_dates: Optional[List[ReleaseDate]] = None
    screenshots: Optional[List[Screenshot]] = None
    summary: Optional[str] = None
    url: Optional[str] = None
    checksum: Optional[str] = None


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
