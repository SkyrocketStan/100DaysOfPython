import requests

API_URL = "https://opentdb.com/api.php?amount=10&type=boolean"


def get_data(url: str = API_URL) -> list:
    data = requests.get(url)
    data.raise_for_status()
    if data.status_code != 200:
        return []
    return data.json()["results"]
