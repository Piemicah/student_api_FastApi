from typing import Generator

from data.base import Base
from sqlalchemy import URL, create_engine, engine
from sqlalchemy.orm import sessionmaker, Session


url = URL.create(
    drivername="postgresql+psycopg2",
    username="postgres",
    password="goodpie222",
    host="localhost",
    port=5432,
    database="student_db",
)

engine = create_engine(url, echo=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = Base


def get_sessionLocal():
    return SessionLocal()


def get_session() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
