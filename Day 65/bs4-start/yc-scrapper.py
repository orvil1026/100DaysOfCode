from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_homepage = response.text

soup = BeautifulSoup(yc_homepage, 'html.parser')

title = []
link = []
upvotes = []

articles = soup.find_all(name='a', class_='storylink')

for article in articles:
    article_text = article.getText()
    title.append(article_text)
    article_link = article.get('href')
    link.append(article_link)

scores = soup.find_all(name='span', class_='score')
upvotes = [int(score.getText().split()[0]) for score in scores]

highest_score = max(upvotes)
highest_index = upvotes.index(highest_score)

# print(upvotes,index)
# print(upvotes[22])

print(title[highest_index])
print(link[highest_index])
print(upvotes[highest_index])
# print(soup.prettify())