import requests

PIXELA_API_TOKEN = "wVcvGqkpXFNvHK5o7aCtsUHpD"
PIXELA_API_URL = "https://pixe.la/v1/users"
PIXELA_API_USERNAME = "anonymous101284"
post_params = {"token": PIXELA_API_TOKEN,
               "username": PIXELA_API_USERNAME,
               "agreeTermsOfService": "yes",
               "notMinor": "yes"}
response = requests.post(PIXELA_API_URL, json=post_params)
print(response.text)
#
#
# delete_params = {"X-USER-TOKEN": PIXELA_API_TOKEN}
# delete_url = PIXELA_API_URL + "/" + PIXELA_API_USERNAME
# response = requests.delete(delete_url, json=delete_params)
# print(response.text)
