import requests

base_url = "http://127.0.0.1:8000"

def main():
    artist_name = input("Enter artist name: ")
    response = requests.get(f"{base_url}/artists/{artist_name}")
    print(response.json())

    artist_id = input("Enter artist ID: ")
    response = requests.get(f"{base_url}/albums/{artist_id}")
    print(response.json())

    album_id = input("Enter album ID: ")
    response = requests.get(f"{base_url}/tracks/{album_id}")
    print(response.json())

if __name__ == "__main__":
    main()

