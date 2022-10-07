
import re
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

def data_link(): # Эта функция должно подставлять в запрос URL адресс в таком ввиде https://www.restoclub.ru/spb/place/porto-19
    link = pd.read_csv(open('cards.csv', 'r', encoding='UTF-8'), sep=';')
    web_link = link[['Ссылка на заведение']]
    data_link = web_link.to_string(header=False, index=False)
    data = data_link.split()
    return data
 
URL =['https://www.restoclub.ru/spb/place/big-gvozdec', 'https://www.restoclub.ru/spb/place/delice-3', 'https://www.restoclub.ru/spb/place/1-2-of-you-3']

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0'
}
def all_url():
    for url in range(len(URL)):
        req = requests.get(URL[url],timeout=5, headers=HEADERS)
        soup = bs(req.text, 'html.parser')
        items = soup.find_all('div', class_='page__wrapper')
        adress = []
        for item in items:
            adress.append(
                {
                    'title': item.find('div', class_='place-map').get('data-address')
                }
            )
            time.sleep(1)
        print(adress)

all_url()