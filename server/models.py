from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class Artist(Base):
    __tablename__ = "artists"

    artistid = Column(Integer, primary_key=True)
    name = Column(String)


class Album(Base):
    __tablename__ = "albums"

    albumid = Column(Integer, primary_key=True)
    title = Column(String)
    artistid = Column(Integer)

    # Ajout d'une relation aux pistes
    tracks = relationship("Track", back_populates="album")


class Track(Base):
    __tablename__ = "tracks"

    trackid = Column(Integer, primary_key=True)
    name = Column(String)
    albumid = Column(Integer, ForeignKey("albums.albumid"))

    # Ajout d'une relation à l'album
    album = relationship("Album", back_populates="tracks")
