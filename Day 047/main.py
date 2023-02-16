import smtplib

import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/NESCO-NPC-9-Pressure-Canner-Stainless/dp/B07VL6LX7V"
UA = "MMozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5)" \
     "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15"
AL = "en-US"
BUY_PRICE = 200
SMTP_ADDRESS = "smtp"
EMAIL = "noob@no.pe"
PASSWORD = "password"


def get_html_data():
    headers = {"Accept-Language": AL, "User-Agent": UA}
    response = requests.get(URL, headers=headers)
    response.raise_for_status()
    return response.text


data = get_html_data()
soup = BeautifulSoup(data, "lxml")
price = soup.find(name="span", class_="a-offscreen") \
    .getText().strip().replace("$", "")
title = soup.find(id="productTitle").get_text().strip()


# print(title)
# print(price)

def sent_email():
    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )
        print(result)


if float(price) < BUY_PRICE:
    message = f"{title} is now {price}"
    sent_email()
