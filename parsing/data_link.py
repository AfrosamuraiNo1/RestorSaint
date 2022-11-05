import pandas as pd
import pathlib
from pathlib import Path


data_csv = Path(pathlib.Path.home(),'projects','learn-web','data_csv','cards.csv')


def data_link(): # Эта функция должна подставлять в запрос URL адресс в таком ввиде https://www.restoclub.ru/spb/place/porto-19
    link = pd.read_csv(open(data_csv, 'r', encoding='UTF-8'), sep=';')
    web_link = link[['Ссылка на заведение']]
    data_link = web_link.to_string(header=False, index=False)
    data = data_link.split()
    return data