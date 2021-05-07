from bs4 import BeautifulSoup
import requests
from requests.api import request
import lxml

class Product:
    def __init__(self, url, title, reviews_list, price,star, image_url=None):
        self.url = url
        self.title = title
        self.reviews_list = reviews_list
        self.price = price
        self.image_url = image_url
        self.star = star

    def print(self):
        print(f"Title={self.title}\nReviews={self.reviews_list}\n price={self.price}\n star={self.star} \nURL={self.url}")


class Scrapper:
    def __init__(self):
        self.base_url = "https://www.amazon.in"
        self.middle_url = "/s?k="
        self.end_url = "&ref=nb_sb_noss_2"
        self.href_list = []
        self.object_list = []

    def get_soup(self,url):
        
        
        header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
        }

        response = requests.get(url, headers=header)

        soup = BeautifulSoup(response.content, 'lxml')
        return soup
    

    def get_links(self,search_word):

        search_word = search_word.replace(' ',"+").strip()
        
        url = self.base_url + self.middle_url + search_word + self.end_url


        soup = self.get_soup(url)
        products = soup.find_all(name='span', class_="a-size-medium a-color-base a-text-normal")
        links = soup.find_all(name='a',class_="a-link-normal a-text-normal")[:4]

        # for product in products:
        #     title = product.getText()
        #     print(f"{title}\n")

        
        for link in links:
            
            href = link.get('href')
            self.href_list.append(href)

        return self.href_list
    
# print(product)
    def get_object_list(self,link_list):
        
        for link in link_list:
            url = self.base_url + link
            soup = self.get_soup(url)

            title = soup.find(id="productTitle").getText()
            

            try:
                price = soup.find(id="priceblock_ourprice").getText()
                
            except:
                price = "NA"
                

            star = soup.find(class_="a-icon-alt").getText()
            

            reviews = soup.find_all(class_="a-expander-content reviewText review-text-content a-expander-partial-collapse-content")

            review_list = []
            for review in reviews:
                review_list.append(review.getText())
                


            product = Product(url=link, title=title.strip(), reviews_list=review_list, price=price, star=star)
            self.object_list.append(product)

        return self.object_list




