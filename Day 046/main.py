import requests
from bs4 import BeautifulSoup

date = input(
    "Which year do you want to travel to? Type the date in this format "
    "YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
response.raise_for_status()
soup = BeautifulSoup(response.text, 'html.parser')
song_names_raw = soup.find_all("h3", class_="a-no-trucate")
song_names = [song.getText().strip() for song in song_names_raw]
print(song_names)
