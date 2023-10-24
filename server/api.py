# Import FastAPI for building the API, SQLAlchemy for database operations, and Pydantic for data validation
from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from .database import create_db_session, create_db_engine
from .models import Artist, Album, Track
from pydantic import BaseModel

# Create a FastAPI instance
app = FastAPI()

# Database configuration: Use SQLite and create an engine and session
db_url = "sqlite:///./chinook.db"
engine = create_db_engine(db_url)
session = create_db_session(engine)


# Define an endpoint to get artists by name
@app.get("/artists/{artist_name}")
def get_artists(artist_name: str):
    # Query the database for artists containing the provided name
    artists = session.query(Artist).filter(Artist.name.contains(artist_name)).all()

    # Raise an exception if no artists are found
    if not artists:
        raise HTTPException(status_code=404, detail="Artist not found")

    # Return a list of dictionaries with artist information
    return [{"artist_id": artist.artistid, "name": artist.name} for artist in artists]


# Define an endpoint to get albums by artist ID
@app.get("/albums/{artist_id}")
def get_albums(artist_id: int):
    # Query the database for albums of the specified artist ID
    albums = session.query(Album).filter(Album.artistid == artist_id).all()

    # Raise an exception if no albums are found
    if not albums:
        raise HTTPException(status_code=404, detail="Albums not found")

    # Return a list of dictionaries with album information
    return [{"album_id": album.albumid, "title": album.title} for album in albums]


# Define an endpoint to get tracks by album ID
@app.get("/tracks/{album_id}")
def get_tracks(album_id: int):
    # Query the database for tracks of the specified album ID
    tracks = session.query(Track).filter(Track.albumid == album_id).all()

    # Raise an exception if no tracks are found
    if not tracks:
        raise HTTPException(status_code=404, detail="Tracks not found")

    # Return a list of dictionaries with track information
    return [{"track_id": track.trackid, "name": track.name} for track in tracks]


# Pydantic model for creating an artist
class ArtistCreate(BaseModel):
    name: str


# Define an endpoint to create a new artist
@app.post("/artists/")
def create_artist(artist: ArtistCreate):
    # Create a new artist instance and add it to the database
    new_artist = Artist(name=artist.name)
    session.add(new_artist)
    session.commit()
    session.refresh(new_artist)
    return new_artist


# Define an endpoint to update an artist by ID
@app.put("/artists/{artist_id}")
def update_artist(artist_id: int, new_name: str):
    # Query the database for the artist to update
    artist = session.query(Artist).filter(Artist.artistid == artist_id).first()

    # Raise an exception if the artist is not found
    if artist is None:
        raise HTTPException(status_code=404, detail="Artist not found")

    # Update the artist's name, commit changes, and refresh the session
    artist.name = new_name
    session.commit()
    session.refresh(artist)
    return artist


# Define an endpoint to delete an artist by ID
@app.delete("/artists/{artist_id}")
def delete_artist(artist_id: int):
    # Query the database for the artist to delete
    artist = session.query(Artist).filter(Artist.artistid == artist_id).first()

    # Raise an exception if the artist is not found
    if artist is None:
        raise HTTPException(status_code=404, detail="Artist not found")

    # Delete the artist, commit changes, and return a success message
    session.delete(artist)
    session.commit()
    return {"message": "Artist deleted successfully"}
