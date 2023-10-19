from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base


def create_db_engine(dase_url):
    engine = create_engine(dase_url)
    return engine


def create_db_session(engine):
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    return Session()
