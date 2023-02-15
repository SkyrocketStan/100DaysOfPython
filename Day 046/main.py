import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

date = input(
    "Which year do you want to travel to? Type the date in this format "
    "YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')
song_names_raw = soup.find_all("h3", class_="a-no-trucate")
song_names = [song.getText().strip() for song in song_names_raw]
print(song_names)

SPOTIPY_CLIENT_ID = "YOUR-SPOTIPY_CLIENT_ID"
SPOTIPY_CLIENT_SECRET = "YOUR-SPOTIPY_CLIENT_SECRET"
SPOTIPY_REDIRECT_URI = "http://localhost:8888/callback"  # here you need to put the same URI in your Spotify account

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="user-library-read playlist-modify-private",
        redirect_uri=SPOTIPY_REDIRECT_URI,
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=False,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]
date = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
