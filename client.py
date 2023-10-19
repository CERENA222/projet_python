import requests

base_url = "http://127.0.0.1:8000"


def get_artists_by_name(artist_name: str):
    response = requests.get(f"{base_url}/artists/{artist_name}")
    print(response.json())


def get_albums_by_artist_id(artist_id: int):
    response = requests.get(f"{base_url}/albums/{artist_id}")
    print(response.json())


def get_tracks_by_album_id(album_id: int):
    response = requests.get(f"{base_url}/tracks/{album_id}")
    print(response.json())


def create_artist(name: str):
    response = requests.post(f"{base_url}/artists/", json={"name": name})
    print(response.json())


def update_artist(artist_id: int, new_name: str):
    response = requests.put(
        f"{base_url}/artists/{artist_id}", json={"new_name": new_name}
    )
    print(response.json())


def delete_artist(artist_id: int):
    response = requests.delete(f"{base_url}/artists/{artist_id}")
    print(response.json())


def main():
    artist_name = input("Enter artist name: ")
    get_artists_by_name(artist_name)

    artist_id = input("Enter artist ID: ")
    get_albums_by_artist_id(artist_id)

    album_id = input("Enter album ID: ")
    get_tracks_by_album_id(album_id)

    new_artist_name = input("Enter new artist name for creation: ")
    create_artist(new_artist_name)

    artist_id_to_update = input("Enter artist ID for update: ")
    new_artist_name = input("Enter new artist name: ")
    update_artist(artist_id_to_update, new_artist_name)

    artist_id_to_delete = input("Enter artist ID for deletion: ")
    delete_artist(artist_id_to_delete)

    # Ajoutez des appels aux nouvelles fonctionnalités de modification
    # (création, mise à jour, suppression) pour les albums et les pistes si nécessaire


if __name__ == "__main__":
    main()
