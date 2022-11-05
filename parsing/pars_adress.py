from cgitb import html
from signal import pause
import requests
from bs4 import BeautifulSoup as BS
import csv
import time
from data_link import data_link
import pathlib
from pathlib import Path


CSV = Path(pathlib.Path.home(),'projects','learn-web','data_csv','adress.csv')

HOST = 'https://www.restoclub.ru'
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0'
}


def get_html(url, params=''):
    r = requests.get(url, timeout=5, headers=HEADERS, params=params)
    return r


def get_content(html): 
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='page__wrapper')
    adress = []

    for item in items:
        adress.append(
            {
                'name': item.find('span', class_='header__title').get_text(),
                'title': item.find('div', class_='place-map').get('data-address'),
                'about': item.find('div', class_='expandable-text__t').get_text()
            }
        )
    return adress


def save_doc(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название организации','Адрес заведения','Описание заведения'])
        for item in items:
            writer.writerow([item['name'],item['title'], item['about']])


def parser():
    adress = []
    URL = data_link()
    for url in URL:
        html = get_html(url)
        if html.status_code == 200:
            adress.extend(get_content(html.text))
            print('Создана точка.')    
        else:
            print('Error')
        time.sleep(1)
    save_doc(adress, CSV)

if __name__ == "__main__":
    parser()