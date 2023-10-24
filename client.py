# Import the 'requests' module for making HTTP requests
import requests

# Base URL for the API
base_url = "http://127.0.0.1:8000"


# Function to retrieve artists by name
def get_artists_by_name(artist_name: str):
    response = requests.get(f"{base_url}/artists/{artist_name}")
    print(response.json())


# Function to retrieve albums by artist ID
def get_albums_by_artist_id(artist_id: int):
    response = requests.get(f"{base_url}/albums/{artist_id}")
    print(response.json())


# Function to retrieve tracks by album ID
def get_tracks_by_album_id(album_id: int):
    response = requests.get(f"{base_url}/tracks/{album_id}")
    print(response.json())


# Function to create a new artist
def create_artist(name: str):
    response = requests.post(f"{base_url}/artists/", json={"name": name})
    print(response.json())


# Function to update an artist
def update_artist(artist_id: int, new_name: str):
    response = requests.put(
        f"{base_url}/artists/{artist_id}", json={"new_name": new_name}
    )
    print(response.json())


# Function to delete an artist
def delete_artist(artist_id: int):
    response = requests.delete(f"{base_url}/artists/{artist_id}")
    print(response.json())


# Main function
def main():
    # Ask the user to input an artist name and display the results
    artist_name = input("Enter artist name: ")
    get_artists_by_name(artist_name)

    # Ask the user to input an artist ID and display the corresponding albums
    artist_id = input("Enter artist ID: ")
    get_albums_by_artist_id(artist_id)

    # Ask the user to input an album ID and display the corresponding tracks
    album_id = input("Enter album ID: ")
    get_tracks_by_album_id(album_id)

    # Ask the user to input the name of a new artist and create the artist
    new_artist_name = input("Enter new artist name for creation: ")
    create_artist(new_artist_name)

    # Ask the user to input the ID of an artist to update and perform the update
    artist_id_to_update = input("Enter artist ID for update: ")
    new_artist_name = input("Enter new artist name: ")
    update_artist(artist_id_to_update, new_artist_name)

    # Ask the user to input the ID of an artist to delete and delete the artist
    artist_id_to_delete = input("Enter artist ID for deletion: ")
    delete_artist(artist_id_to_delete)

    # Add calls to new modification features (creation, update, deletion) for albums and tracks if necessary


# Check if the script is being run as the main program
if __name__ == "__main__":
    # Execute the main function
    main()
