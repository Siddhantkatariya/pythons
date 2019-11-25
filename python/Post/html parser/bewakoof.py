import requests
from bs4 import BeautifulSoup

req= requests.get('https://www.bewakoof.com/')
bs = BeautifulSoup(req.content,'html.parser')
fp=open('file_name.csv','w')
fp.write('t-shirt name ,price, image\n')


for product in bs.find_all('div',{'class': 'productCardBox'}):
    for detail in product.find_all('div',{'class': 'productCardBox'}):
        print(detail.find_all('b'))
        fp.write(',')
        fp.write(str(detail.find_all('b')[0].text))
        fp.write(',')
        fp.write('\n')
        fp.close()


# print(title)