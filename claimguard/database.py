from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from claimguard.settings import Settings

engine = create_engine(Settings().DATABASE_URL)

def get_session():
    with Session(engine) as session:
        yield session

@contextmanager
def get_session_job():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()
        