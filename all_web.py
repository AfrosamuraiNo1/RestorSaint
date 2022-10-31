
from hashlib import new
import pandas as pd
from collections import defaultdict
import re


def data_address(): # Эта функция должна обрабатывать адреса ("Тихоокеанская ул., 10, Санкт-Петербург")
    link = pd.read_csv(open("data_csv/adress.csv", 'r', encoding='UTF-8'), sep=';')
    web_link = link.set_index('Название организации').to_dict()['Адрес заведения']
    reverse = defaultdict(list)
    for key, value in web_link.items():
        if 'г.' in value:
            del value
        else:
            value = value.lstrip() + ', Санкт-Петербург'
            reverse[key].append(value)
            patern = '(\S+\s)(\w+\S\D)(\D+)(\d+)(\S+)'
            repl = r'\4\5 \1\2\3'
            text = reverse.values()
    print(text)
            # for item in text:  #меняет адреса ставя номер дома спереди.
            #     print(item)
    #             if re.match(patern,item):
    #                 new_number_house = re.sub(patern,repl,item)
    #                 reverse[key].append(new_number_house)
    #                 print(reverse)

    #                 prospekt = []
    #                 for prosp in number_house: #меняет адреса заменяет "пр." на "проспект".
    #                     if 'пр.' in prosp:
    #                         new_pospekt = re.sub('пр.', 'проспект', prosp)
    #                         prospekt.append(new_pospekt)
    #                     else:
    #                         prospekt.append(prosp)                     
    # return prospekt


data_address()


