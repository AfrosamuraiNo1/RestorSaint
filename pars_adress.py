from cgitb import html
import requests
from bs4 import BeautifulSoup as BS
import csv
from all_web import all_web


CSV = 'adress.csv'

HOST = 'https://www.restoclub.ru'
URL = 'https://www.restoclub.ru/spb/place/settlers'
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0'
}

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='page__wrapper')
    adress = []

    for item in items:
        adress.append(
            {
                'title': item.find('div', class_='place-map').get('data-address')
            }
        )
    return adress

#html = get_html(URL)
#print(get_content(html.text))


def save_doc(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Адрес заведения'])
        for item in items:
            writer.writerow([item['title']])


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        adress = []
        adress.extend(get_content(html.text))
        save_doc(adress, CSV)
        print('Создана точка.')    
    else:
        print('Error')

parser()