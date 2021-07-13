import requests
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = "2e7c4be3a6f847fe9b1d1ec069e91c8b"
STOCK_PRICE_API_KEY = " VZ7B9GF5RLBKLYRU"

MY_EMAIL = "testingmain19@gmail.com"
TARGET_EMAIL = "itshelloworld001@gmail.com"
PASSWORD = "Qwerty@12345"

def send_update(news, change):
    symbol = "DOWN"
    if change > 0:
        symbol = "UP"
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(MY_EMAIL, PASSWORD)
    connection.sendmail(from_addr= MY_EMAIL, to_addrs= TARGET_EMAIL, msg=
                        f"Subject: {STOCK} {symbol}{change_percent}\n\n {news.encode('ascii', 'ignore').decode('ascii')}")

def get_news():
    new_parameters = {
        "q" : COMPANY_NAME,
        "from" : dict_key[0],
        "sortBy" : "relevency",
        "language" : "en",
        "apiKey" : NEWS_API_KEY
    }
    news_sent = ""
    news_response = requests.get(NEWS_ENDPOINT, params=new_parameters)
    news_items = (news_response.json()["articles"][0:3])
    for news in news_items:
        title = (news["title"])
        brief = (news["description"])
        news_sent = news_sent + "Headline\n\n" + title + "\n\n Brief \n\n" + brief + "\n\n"
    return news_sent


stock_price_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "interval" : "60min",
    "apikey" : STOCK_PRICE_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=stock_price_params)
data = (response.json()["Time Series (Daily)"])
dict_key = list(data.keys())
yesterday_closing_price = float(data[dict_key[0]]["4. close"])
day_before_yesterday =float(data[dict_key[1]]["4. close"])
change_percent = round(((yesterday_closing_price - day_before_yesterday)/day_before_yesterday)*100, 2)

if (change_percent > 0.50):
    news = get_news()
    send_update(news, change_percent)



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



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

