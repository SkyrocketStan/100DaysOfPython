import os

import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()  # This reads the environment variables inside .env

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_TOKEN = os.getenv("ALPHAVANTAGE")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
VIRTUAL_TWILIO_NUMBER = os.getenv("VIRTUAL_TWILIO_NUMBER")
VERIFIED_NUMBER = os.getenv("VERIFIED_NUMBER")


def get_stock_percentage() -> float:
    stock_params = {"function": "TIME_SERIES_DAILY_ADJUSTED",
                    "symbol": STOCK_NAME,
                    "apikey": STOCK_TOKEN}
    stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
    stock_response.raise_for_status()
    stock_list = list(stock_response.json()["Time Series (Daily)"].values())[:2]
    stock_yesterday = float(stock_list[0]["4. close"])
    stock_before_yesterday = float(stock_list[0]["4. close"])
    print(stock_yesterday, stock_before_yesterday)
    stock_difference = abs(stock_yesterday - stock_before_yesterday)
    stock_difference_percentage = (stock_difference / stock_yesterday) * 100
    return stock_difference_percentage


if get_stock_percentage() > 5:
    print("Get News")

# STEP 2: https://newsapi.org/ Instead of printing ("Get News"), actually get
# the first 3 news pieces for the COMPANY_NAME.

# I STUCK HERE! I Can't get the API
# You didn't pass the captcha. Please try again.
# So below is the code from end of lesson


up_down = None
diff_percent = get_stock_percentage()

# # STEP 2: Instead of printing ("Get News"), actually get the first 3 news
# pieces for the COMPANY_NAME.

# Instead of printing ("Get News"), use the News API to get articles related
# to the COMPANY_NAME. If difference percentage is greater than 5 then print(
# "Get News").
if abs(diff_percent) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    # Use Python slice operator to create a list that contains the first 3
    # articles. Hint: https://stackoverflow.com/questions/509211
    # /understanding-slice-notation
    three_articles = articles[:3]
    print(three_articles)

    # # STEP 3: Use Twilio to send a seperate message with each article's
    # title and description to your phone number.

    # Create a new list of the first 3 article's headline and description
    # using list comprehension.
    formatted_articles = [
        f"{STOCK_NAME}: {up_down}{diff_percent}%\n"
        f"Headline: {article['title']}. \n"
        f"Brief: {article['description']}"
        for article in three_articles]
    print(formatted_articles)
    # Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    # Send each article as a separate message via Twilio.
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )
