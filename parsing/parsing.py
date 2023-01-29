import requests
from bs4 import BeautifulSoup as BS
import csv

# Парсинг главной страницы.
# Parsing first list 
CSV = 'cards.csv'

HOST = 'https://www.restoclub.ru'
URL = 'https://www.restoclub.ru/spb/search/novie-restorany-cafe-i-bary-v-peterburge'
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0'
}


def get_html(url, params=''):
    response = requests.get(url, headers=HEADERS, params=params)
    return response


def get_content(html):
    soup = BS(html, 'html.parser')
    items = soup.find_all('div', class_='search-place-card')
    cards = []

    for item in items:
        cards.append(
            {
                'title': item.find('span', class_='search-place-title__name').get_text(strip=True),
                'link_restaran': HOST + item.find('a', class_='search-place-title__link').get('href'),
                'about': item.find('div', class_='search-place-card__about').get_text(strip=True),
                'card_img': item.find('a', class_='gallery-photo _cover _lazy').find('source').get('data-src')
            }
        )
    return cards


def save_doc(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название заведения', 'Ссылка на заведение',
                        "Информация о заведение", "Лого заведения"])
        for item in items:
            writer.writerow(
                [item['title'], item['link_restaran'], item['about'], item['card_img']])


def parser():
    PAGENATION = input('Укажите количество страниц для парсинга: ')
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        for page in range(1, PAGENATION + 1):
            print(f'Парсинг страницы: {page}')
            html = get_html(URL, params={'page': page})
            cards.extend(get_content(html.text))
            save_doc(cards, CSV)
        print('Конец парсинга.')
    else:
        print('Error')


parser()
