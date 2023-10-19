from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session
from .database import create_db_session, create_db_engine
from .models import Artist, Album, Track

app = FastAPI()

# Configuration de la base de données
dase_url = "sqlite:///./chinook.db"
engine = create_db_engine(dase_url)
session = create_db_session(engine)


# Route pour obtenir les artistes par nom
@app.get("/artists/{artist_name}")
def get_artists(artist_name: str):
    artists = session.query(Artist).filter(Artist.name.contains(artist_name)).all()
    if not artists:
        raise HTTPException(status_code=404, detail="Artist not found")

    return [{"artist_id": artist.artistid, "name": artist.name} for artist in artists]


# Route pour obtenir les albums par ID d'artiste
@app.get("/albums/{artist_id}")
def get_albums(artist_id: int):
    albums = session.query(Album).filter(Album.artistid == artist_id).all()
    if not albums:
        raise HTTPException(status_code=404, detail="Albums not found")

    return [{"album_id": album.albumid, "title": album.title} for album in albums]


# Route pour obtenir les noms de pistes par ID d'album
@app.get("/tracks/{album_id}")
def get_tracks(album_id: int):
    tracks = session.query(Track).filter(Track.albumid == album_id).all()
    if not tracks:
        raise HTTPException(status_code=404, detail="Tracks not found")

    return [{"track_id": track.trackid, "name": track.name} for track in tracks]


