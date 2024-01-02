from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./romarr.db"


class Database:
    def __init__(self):
        self.engine = None
        self.SessionLocal = None
        self.Base = None

    def create_all(self):
        self.engine = create_engine(
            SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
        )
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

        self.Base = declarative_base()

    def add_to_db(self, db_object):
        db = self.SessionLocal()
        db.add(db_object)
        db.commit()
        db.refresh(db_object)
        db.close()

    def remove_from_db(self, db_object):
        db = self.SessionLocal()
        db.delete(db_object)
        db.commit()
        db.close()
