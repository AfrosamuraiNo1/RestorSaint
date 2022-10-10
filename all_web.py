
from hashlib import new
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

def data_address(): # Эта функция должна обрабатывать адреса ("Тихоокеанская ул., 10, Санкт-Петербург")
    link = pd.read_csv(open('adress.csv', 'r', encoding='UTF-8'), sep=';')
    web_link = link[['Адрес заведения']]
    data_link = web_link.to_string(header=False, index=False)
    for data in data_link:
        data = data_link.split('\n')
        city_data = []
        for address in data:
            if 'г.' in address:
                del address
            else:
                address = address.lstrip() + ', Санкт-Петербург'
                city_data.append(address)
        return city_data

print(data_address())
 