from bs4 import BeautifulSoup
import requests
import lxml


#BTC rate
url_bitcoin = 'https://coinmarketcap.com/currencies/bitcoin/'
response_bitcoin= requests.get(url_bitcoin)
soup_bitcoin = BeautifulSoup(response_bitcoin.text, 'lxml')
bitcoin_rate = soup_bitcoin.find('div', class_='priceValue___11gHJ').text
main_bitcoin_rate = "".join(bitcoin_rate.split(","))
title_bitcoin = soup_bitcoin.find('h2', class_="sc-1q9q90x-0 iYFMbU h1___3QSYG").find('small', class_="nameSymbol___1arQV").text
print(f'Курс {title_bitcoin}:{main_bitcoin_rate}')

#ETC rate
url_ethereum = 'https://coinmarketcap.com/currencies/ethereum/'
response_ethereum = requests.get(url_ethereum)
soup_ethereum= BeautifulSoup(response_ethereum.text, 'lxml')
ethereum_rate = soup_ethereum.find('div', class_='priceValue___11gHJ').text
main_ethereum_rate = "".join(ethereum_rate.split(","))
title_ethereum = soup_ethereum.find('h2', class_="sc-1q9q90x-0 iYFMbU h1___3QSYG").find('small', class_="nameSymbol___1arQV").text
print(f'Курс {title_ethereum}:{main_ethereum_rate}')

#XRP rate
url_xrp = 'https://coinmarketcap.com/currencies/xrp/'
response_xrp = requests.get(url_xrp)
soup_xrp = BeautifulSoup(response_xrp.text, 'lxml')
xrp_rate = soup_xrp.find('div', class_='priceValue___11gHJ').text
main_xrp_rate = "".join(xrp_rate.split(","))
title_xrp = soup_xrp.find('h2', class_="sc-1q9q90x-0 iYFMbU h1___3QSYG").find('small', class_="nameSymbol___1arQV").text
print(f'Курс {title_xrp}:{main_xrp_rate}')

#ADA(cardano) rate
url_cardano = 'https://coinmarketcap.com/currencies/cardano/'
response_cardano = requests.get(url_cardano)
soup_cardano = BeautifulSoup(response_cardano.text, 'lxml')
cardano_rate = soup_cardano.find('div', class_='priceValue___11gHJ').text
main_cardano_rate = "".join(cardano_rate.split(","))
title_cardano = soup_cardano.find('h2', class_="sc-1q9q90x-0 iYFMbU h1___3QSYG").find('small', class_="nameSymbol___1arQV").text
print(f'Курс {title_cardano}:{main_cardano_rate}')

crypto_rating = f'Курс {title_bitcoin} : {main_bitcoin_rate}\nКурс {title_ethereum} : {main_ethereum_rate}\nКурс {title_xrp} : {main_xrp_rate}\nКурс {title_cardano} : {main_cardano_rate}'






