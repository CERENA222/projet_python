# Import necessary modules from SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base


# Function to create a database engine
def create_db_engine(db_url):
    # Create an SQLAlchemy engine using the provided database URL
    engine = create_engine(db_url)
    return engine


# Function to create a database session
def create_db_session(engine):
    # Create the database tables defined in the models using the provided engine
    Base.metadata.create_all(bind=engine)

    # Create a sessionmaker bound to the engine for interacting with the database
    Session = sessionmaker(bind=engine)
    return Session()
