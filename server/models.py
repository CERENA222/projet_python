# Import necessary modules from SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Create a base class for declarative models
Base = declarative_base()


# Define the Artist model, representing the 'artists' table
class Artist(Base):
    __tablename__ = "artists"

    # Define columns for the 'artists' table
    artistid = Column(Integer, primary_key=True)  # Primary key for the artist
    name = Column(String)  # Artist's name


# Define the Album model, representing the 'albums' table
class Album(Base):
    __tablename__ = "albums"

    # Define columns for the 'albums' table
    albumid = Column(Integer, primary_key=True)  # Primary key for the album
    title = Column(String)  # Album title
    artistid = Column(Integer)  # Foreign key referencing the 'artists' table

    # Establish a relationship with the 'tracks' table
    tracks = relationship("Track", back_populates="album")


# Define the Track model, representing the 'tracks' table
class Track(Base):
    __tablename__ = "tracks"

    # Define columns for the 'tracks' table
    trackid = Column(Integer, primary_key=True)  # Primary key for the track
    name = Column(String)  # Track name
    albumid = Column(
        Integer, ForeignKey("albums.albumid")
    )  # Foreign key referencing the 'albums' table

    # Establish a relationship with the 'albums' table
    album = relationship("Album", back_populates="tracks")
