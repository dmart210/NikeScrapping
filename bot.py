from bs4 import *
import requests 
from twilio.rest import Client

account_sid = 'ACef937e0e56d71010db4e6605ad85f163'
auth_token = '6a546b2857644b82865b647d8e41f8d5'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body = "Yerrr",
    from_ = '+17853478886',
    to = '+13472839986'  
)

message2 = client.messages.create(
    body = "what ",
    from_ = '+17853478886',
    to = '+13472839986'  
)

url = 'https://www.cnbc.com/quotes/NKE'
r  = requests.get(url)
stat = r.status_code
if stat != 200:
    exit()
stock_text = r.text
soup = BeautifulSoup(stock_text, 'lxml')
price = soup.find('span', {'class':'QuoteStrip-lastPrice'}).text
if float(price) < float('5'):
    message.sid
else:
    message2.sid