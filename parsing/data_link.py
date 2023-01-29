import pandas as pd
import pathlib
from pathlib import Path


# Берет нужные ссылки из cards.csv.
# Take the necessary links
data_csv = Path(pathlib.Path.home(), 'projects', 'learn-web',
                'utils', 'data_csv', 'cards.csv')

# Эта функция должна подставлять в запрос URL адресс в таком ввиде https://www.restoclub.ru/spb/place/porto-19
# This function should substitute in requests URL address. Like this https://www.restoclub.ru/spb/place/porto-19
def data_link():
    link = pd.read_csv(open(data_csv, 'r', encoding='UTF-8'), sep=';')
    web_link = link[['Ссылка на заведение']]
    data_link = web_link.to_string(header=False, index=False)
    data = data_link.split()
    return data
