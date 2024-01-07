import requests
from bs4 import BeautifulSoup

amazonUrl = 'https://www.amazon.in/s?k='
userAgent = 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0'

headers = {'User-Agent': userAgent}

response = requests.get(amazonUrl)
response = requests.get(amazonUrl, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

class Shoppping:
    def __init__(self, productName):
        self.productName = productName;

    def amazonShopping(self):
       url = f"https://www.amazon.in/s?k={self.productName}"
       response = requests.get(url, headers=headers)
       soup = BeautifulSoup(response.content, 'html.parser')

       prices = soup.find_all(class_='a-price-whole')
       links = soup.find_all(class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')
       images = soup.find_all(class_='s-image')
       product_name = soup.find_all(class_='a-size-medium a-color-base a-text-normal')

       data = []

       for i in range(0, 40):
           try:
               data.append({
                   'id': i,
                   'price': float(prices[i].text.replace(',', '')),
                   'link': "https://amazon.in/" + links[i].get('href'), 
                   'image': images[i].get('src'),
                   'company': 'amazon',
                   'searched_name': self.productName
                   })
           except:
               pass

       return data
