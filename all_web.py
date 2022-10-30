import pandas as pd
from collections import defaultdict
import re


def data_address(): # Эта функция должна обрабатывать адреса ("Тихоокеанская ул., 10, Санкт-Петербург")
    link = pd.read_csv(open("data_csv/adress.csv", 'r', encoding='UTF-8'), sep=';')
    web_link = link.set_index('Название организации').to_dict()['Адрес заведения']
    reverse = defaultdict(list)
    d = []
    for key, value in web_link.items(): #Если в тексте есть город,удаляет строку. Меняет адреса добавляя в конце ' , Санкт-Петербург'.
        if 'г.' in value:
            del value
        else:
            value = value.lstrip() +' , Санкт-Петербург'
            d.append(value)
    print(d)
            # patern = '(\S+\s)(\D+\s)(\d+)(\S+\s)'
            # repl = r'\3 \1\2'
            # text = d 
            # number_house = []
            # for item in text:  #меняет адреса ставя номер дома спереди.
            #     if re.match(patern,item):
            #         new_number_house = re.sub(patern,repl,item)
            #         number_house.append(new_number_house)
                    # prospekt = []
                    # for prosp in number_house: #меняет адреса заменяет "пр." на "проспект".
                    #     if 'пр.' in prosp:
                    #         new_pospekt = re.sub('пр.', 'проспект', prosp)
                    #         prospekt.append(new_pospekt)
                    #     else:
                    #         prospekt.append(prosp)                     
                    #     return prospekt
    #return number_house


# def prospekt():
#     number_house = data_address()
#     prospekt = []
#     for prosp in number_house: #меняет адреса заменяет "пр." на "проспект".
#         print(prosp)
        # if 'пр.' in prosp:
        #     new_pospekt = re.sub('пр.', 'проспект', prosp)
        #     prospekt.append(new_pospekt)
        # else:
        #     prospekt.append(prosp)                     
        # return prospekt

print(data_address())