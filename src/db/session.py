from collections.abc import Generator
from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from src.config import Settings

engine = create_engine(url=Settings().get_database_url(), pool_pre_ping=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def create_db_session() -> Generator[Session, Any, None]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
