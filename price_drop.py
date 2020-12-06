import requests
from bs4 import BeautifulSoup
import time
url = 'https://www.flipkart.com/poco-m2-slate-blue-64-gb/p/itmfd82e37cf60fb'
res = requests.get(url).content
soup = BeautifulSoup(res, 'lxml')
original_price = soup.find('div', class_='_30jeq3 _16Jk6d').text
original_price = original_price.replace(',', '')
original_price = int(original_price[1:])
print(f'original price is {original_price}')


def check_price():
    url = 'https://www.flipkart.com/poco-m2-slate-blue-64-gb/p/itmfd82e37cf60fb'
    res = requests.get(url).content
    soup = BeautifulSoup(res, 'lxml')
    price = soup.find('div', class_='_30jeq3 _16Jk6d').text
    print(price)
    price = price.replace(',', '')
    return int(price[1:])

if __name__ == '__main__':
    while True:
        current_price = check_price()
        print(f'currenty price is:{current_price}')
        if current_price < original_price:
            print(
                f'price decreased by {(original_price-current_price)*100/original_price}')
        else:
            print('price not decreased')
        time.sleep(60)