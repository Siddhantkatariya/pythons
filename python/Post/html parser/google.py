import requests
from bs4 import BeautifulSoup




req= requests.get('https://www.bewakoof.com/')
bs = BeautifulSoup(req.content,'html.parser')
# fp=open('file_name..csv','w')


# for product in bs.find_all('div')
# title =bs.find_all('div',{'class': 'productCardBox'})
# print(title)

for i in bs.find_all('a'):
    print(i['href'])

