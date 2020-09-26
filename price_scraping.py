from bs4 import BeautifulSoup
import requests
import time

url = 'https://www.hepsiburada.com/asus-pa27ac-27-5ms-hdmix2-display-full-hd-ips-hdr1000-monitor-p-HBV00000AJ3Q2'
headers = {"User-Agent":'Mozilla/5.0 (X11; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}

def checkPrice():
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="product-name",class_="product-name best-price-trick").text.strip() #extracing only the text
    price = soup.find(id="offering-price").text[0:6].strip() #converting useful part of the price
    limit = str(price) #set price limit to check changes

    if str(price) < limit:
        print(f'TITLE: {title} \nPRICE: {price} TL\nPRICE HAS DECREASED! \n',url)
    elif str(price) > limit:
        print(f'TITLE: {title}\nPRICE: {price} TL\nPRICE HAS INCREASED!')
    else:
        print(f'PRICE: {price} TL\nPRICE HAS NOT CHANGE!')

while True: #checking the price for every 24 hours
    checkPrice()
    time.sleep(86400)