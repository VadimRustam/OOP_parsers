from db.settings import settings
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from contextlib import contextmanager
from sqlalchemy.orm import DeclarativeBase

engine = create_engine(settings.DATABASE_URL_sync())


@contextmanager
def session_db():
    session = Session(bind=engine)
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
    finally:
        session.close()

class Base(DeclarativeBase):
	pass