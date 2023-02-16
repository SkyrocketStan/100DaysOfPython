import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/NESCO-NPC-9-Pressure-Canner-Stainless/dp/B07VL6LX7V"
UA = "MMozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)" \
     "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15"
AL = "en-US"


def get_html_data():
    headers = {"Accept-Language": AL, "User-Agent": UA}
    response = requests.get(URL, headers=headers)
    response.raise_for_status()
    return response.text


data = get_html_data()
soup = BeautifulSoup(data, "lxml")
price = soup.find(name="span", class_="a-offscreen") \
    .getText().strip().replace("$", "")
print(price)
