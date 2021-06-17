
from sys import flags
from bs4 import BeautifulSoup
import requests
import lxml
import math


url = 'https://coinmarketcap.com/ru/currencies/bitcoin/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml')


btc_rate = soup.find('div', class_='priceValue___11gHJ').text.split()
title = soup.find('h1', class_="priceHeading___2GB9O").find('small', recursive=False)

print(btc_rate, title.text)






