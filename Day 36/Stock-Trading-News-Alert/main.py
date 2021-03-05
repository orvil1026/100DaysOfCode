#importing libs
import requests
from decouple import config
from stockdata import recent_data
from twilio.rest import Client

COMPANY_NAME = "Tesla Inc"


# params for newsapi
parameters = {
    'q': COMPANY_NAME,
    'apiKey': config('NEWS_API_KEY')
}
# calling the get function on newsapi
response = requests.get(url='https://newsapi.org/v2/everything', params=parameters)

# getting the json data from response
data = response.json()

# the top three articles
top_five_articles = data['articles'][:3]

# string variable which will contain the news articles
news = ''
for article in top_five_articles:
    news += f"Title:{article['title']}\n"
    news += f"Description:{article['description']}\n\n"
print(news)


# Getting the tsla stock data from tsla_data
yesterday_closing_price = recent_data[0]['4. close']
previous_day_closing_price = recent_data[1]['4. close']
diff = float(yesterday_closing_price) - float(previous_day_closing_price)

updown = ''
if diff < 0:
    updown = '🔻'
else:
    updown = '🔼'

percentage_diff = (abs(diff)/float(yesterday_closing_price)) * 100

# String to store all the stock related data
stock_info = f"\nTSLA {updown}\n"
stock_info += f"Difference:{diff}\nChange Percent:{percentage_diff}"

# print(stock_info)

# final message

message = news + stock_info
# print(message)

account_sid = config("TWILIO_ACCOUNT_SID")
auth_token = config("AUTH_TOKEN")

client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body=message,
         from_='+16235524092',
         to=config('PHONE_NUMBER')
     )

print(message.status)