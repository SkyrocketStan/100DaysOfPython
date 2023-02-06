from datetime import datetime

import requests

PIXELA_API_TOKEN = "wVcvGqkpXFNvHK5o7aCtsUHpD"
HEADERS_TOKEN = {"X-USER-TOKEN": PIXELA_API_TOKEN}
PIXELA_API_URL = "https://pixe.la/v1/users"
USERNAME = "anonymous101284"
HEADERS = {"X-USER-TOKEN": PIXELA_API_TOKEN}
GRAPH_ENDPOINT = f"{PIXELA_API_URL}/{USERNAME}/graphs"


def make_user():
    post_params = {"token": PIXELA_API_TOKEN,
                   "username": USERNAME,
                   "agreeTermsOfService": "yes",
                   "notMinor": "yes"}
    response = requests.post(PIXELA_API_URL, json=post_params)
    print(response.text)


def make_graph():
    graph_config = {
        "id": "whiskeys",
        "name": "Whiskey shots",
        "unit": "shots",
        "type": "int",
        "color": "ajisai"
    }
    response = requests.post(GRAPH_ENDPOINT, json=graph_config, headers=HEADERS)
    print(response.text)


def make_pixel():
    today = datetime.now().strftime("%Y%m%d")
    pixel_endpoint = f"{GRAPH_ENDPOINT}/whiskeys"
    pixel_data = {"date": today, "quantity": "0"}
    response = requests.post(url=pixel_endpoint,
                             json=pixel_data,
                             headers=HEADERS)
    print(response.text)


def delete_user():
    delete_url = f"{PIXELA_API_URL}/{USERNAME}"
    response = requests.delete(delete_url, headers=HEADERS)
    print(response.text)

# make_user()
# make_graph()
# make_pixel()
# delete_user()
