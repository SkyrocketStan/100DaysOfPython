import os

import requests
from dotenv import load_dotenv

load_dotenv()  # This reads the environment variables inside .env

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_TOKEN = os.getenv("ALPHAVANTAGE")


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


if get_stock_percentage() > -1:
    print("Get News")

# STEP 2: https://newsapi.org/ Instead of printing ("Get News"), actually get
# the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get
#  articles related to the COMPANY_NAME.

# TODO 7. - Use Python slice operator to create a list that contains the
#  first 3 articles. Hint: https://stackoverflow.com/questions/509211
#  /understanding-slice-notation


# STEP 3: Use twilio.com/docs/sms/quickstart/python to send a separate
# message with each article's title and description to your phone number.

# TODO 8. - Create a new list of the first 3 article's headline and
#  description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""TSLA: 🔺2% Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (
TSLA)?. Brief: We at Insider Monkey have gone over 821 13F filings that hedge 
funds and prominent investors are required to file by the SEC The 13F filings 
show the funds' and investors' portfolio positions as of March 31st, near the 
height of the coronavirus market crash. or "TSLA: 🔻5% Headline: Were Hedge 
Funds Right About Piling Into Tesla Inc. (TSLA)?. Brief: We at Insider Monkey 
have gone over 821 13F filings that hedge funds and prominent investors are 
required to file by the SEC The 13F filings show the funds' and investors' 
portfolio positions as of March 31st, near the height of the coronavirus 
market crash."""
