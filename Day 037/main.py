import requests

PIXELA_API_TOKEN = "wVcvGqkpXFNvHK5o7aCtsUHpD"
HEADERS_TOKEN = {"X-USER-TOKEN": PIXELA_API_TOKEN}
PIXELA_API_URL = "https://pixe.la/v1/users"
USERNAME = "anonymous101284"
HEADERS = {"X-USER-TOKEN": PIXELA_API_TOKEN}


def make_user():
    post_params = {"token": PIXELA_API_TOKEN,
                   "username": USERNAME,
                   "agreeTermsOfService": "yes",
                   "notMinor": "yes"}
    response = requests.post(PIXELA_API_URL, json=post_params)
    print(response.text)


make_user()
