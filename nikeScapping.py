
import requests
from requests_html import HTML
from bs4 import *
import time


def parsePrice():
    url = 'https://www.cnbc.com/quotes/NKE'
    r  = requests.get(url)
    stat = r.status_code
    if stat != 200:
        exit()
    stock_text = r.text
    soup = BeautifulSoup(stock_text, 'lxml')
    price = soup.find('span', {'class':'QuoteStrip-lastPrice'}).text
    return price

while True:
    time.sleep(5)
    print('The current price of NIKE is: ', str(parsePrice()))

