import requests
from twilio.rest import Client
import os
import json
from datetime import datetime, timedelta, date
STOCK = input("Stock:- ")
COMPANY_NAME = input("Company:- ")
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# TODO:- BEFORE PUSHING THE CODE REMEMBER TO USE ENV VARIABLES
NEWS_API_KEY = "d883270039a24ee3bbe9f123d29dee90"
STOCK_API_KEY = "B0R9Z5DAND0KKHDZ"
TWILIO_ACCOUNT_SID = "account_sid"
TWILIO_AUTH_TOKEN = "account_token"

PARAMS_NEWS = {
    "q": COMPANY_NAME,
    "apiKey":NEWS_API_KEY
}

params_stock = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK,
    "apikey":STOCK_API_KEY
}

# 


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

def get_stock_news(url, params_new):
    response = requests.get(url, params=params_new)
    data = response.json()
    news_list = [{"title":i['title'], "description":i['description']} for i in data["articles"]][0:3]
    # print(news_list)
    # for i in news_list:
    #     print(i)

    return news_list

def price_diff(yesterday_close, dayBefore_yesterday_close):
    PriceDiff = yesterday_close - dayBefore_yesterday_close
    print(f"price diff is {PriceDiff}")
    perc_price_diff = abs(PriceDiff)/yesterday_close * 100
    print(f"The % diff is {perc_price_diff}")
    if PriceDiff >= 0:
        if perc_price_diff > 1.0:
            print("Entering price_diff if")
            news_list = get_stock_news(NEWS_ENDPOINT, PARAMS_NEWS)
            # TODO:- HAVE TO CALL THE TWILIO API
            client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
            for msg in news_list:
                title = msg["title"]
                description = msg["description"]
                message = client.messages.create(body=f"{STOCK}: 🔺 {perc_price_diff}%\nHeadline: {title} \n\nBrief: {description}", from_= +19253954575, to = +918788062819)
                print(message.status)
    else:
        if perc_price_diff > 1.0:
            print("Entering price_diff if below")
            news_list = get_stock_news(NEWS_ENDPOINT, PARAMS_NEWS)
            # TODO:- HAVE TO CALL THE TWILIO API
            client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
            for msg in news_list:
                title = msg["title"]
                description = msg["description"]
                message = client.messages.create(body=f"{STOCK}: 🔻 {perc_price_diff}%\nHeadline: {title} \n\nBrief: {description}", from_= +19253954575, to = +918788062819)
                print(message.status)


def get_stock_closing_price(url, params_stock):
    print("running get_stock_closing_price")
    try:
        response = requests.get(url, params_stock)
        data = response.json()
        print(data)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request exception occurred: {req_err}")

    current_date = date.today()
    yesterday = current_date - timedelta(days=2)
    dayBefore_yesterday = current_date - timedelta(days=3)

    try:
        # print(data["Time Series (Daily)"][str(yesterday)]["4. close"])
        print("in try of get_stock_Clsoing price")
        # print("+++++++++++++++++++++++++++++",data["Time Series (Daily)"][str(yesterday)]["4. close"])
        
        yesterday_close = float(data["Time Series (Daily)"][str(yesterday)]["4. close"])
        dayBefore_yesterday_close = float(data["Time Series (Daily)"][str(dayBefore_yesterday)]["4. close"])
        price_diff(yesterday_close, dayBefore_yesterday_close)
        
    except KeyError:
        # print("entering except")
        yesterday = current_date - timedelta(days=2)
        dayBefore_yesterday = current_date - timedelta(days=3)
        yesterday_close = float(data["Time Series (Daily)"][str(yesterday)]["4. close"])
        dayBefore_yesterday_close = float(data["Time Series (Daily)"][str(dayBefore_yesterday)]["4. close"])
        price_diff(yesterday_close, dayBefore_yesterday_close)
        

get_stock_closing_price(STOCK_ENDPOINT, params_stock)


## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator


# get_stock_news(NEWS_ENDPOINT, params_new)


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

