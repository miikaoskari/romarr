from sqlmodel import SQLModel, Field, create_engine

"""Game table
"""


class GameBase(SQLModel):
    igdb_id: int | None = None
    name: str | None = None
    summary: str | None = None
    cover_url: str | None = None
    first_release_date: int | None = None

class Game(GameBase, table=True):
    """Game model for storing IGDB results."""

    id: int | None = Field(default=None, primary_key=True)


class GameCreate(GameBase):
    pass


class GamePublic(GameBase):
    id: int


"""Platform table
"""


class PlatformBase(SQLModel):
    igdb_id: int | None = Field(default=None, primary_key=True)
    name: str | None = None
    summary: str | None = None


class Platform(PlatformBase, table=True):
    """Platform model for storing IGDB results."""

    id: int | None = Field(default=None, primary_key=True)


class PlatformCreate(PlatformBase):
    pass


class PlatformPublic(PlatformBase):
    id: int


DATABASE_URL = "sqlite:///./romarr.db"
engine = create_engine(DATABASE_URL, echo=False)
SQLModel.metadata.create_all(engine)
