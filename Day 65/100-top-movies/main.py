import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.hollywoodreporter.com/lists/100-best-films-ever-hollywood-favorites-818512")
top_100_movies_page = response.text

soup = BeautifulSoup(top_100_movies_page, 'html.parser')

movie_list = soup.find_all('h1', class_='list-item__title')


list_of_movies = [movie.getText() for movie in movie_list]


print(list_of_movies)

with open('movies.txt', mode='a') as file:
    for movie in list_of_movies:
        file.write(f"{movie}\n")
# print(movie)
#print(soup.prettify())