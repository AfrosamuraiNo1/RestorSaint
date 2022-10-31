import pandas as pd
from collections import defaultdict
import re

#V0.0
# def data_address(): # Эта функция должна обрабатывать адреса ("Тихоокеанская ул., 10, Санкт-Петербург")
#     link = pd.read_csv(open("data_csv/adress.csv", 'r', encoding='UTF-8'), sep=';')
#     web_link = pd.DataFrame(link[['Адрес заведения']])
#     data_link = web_link.to_string(header=False, index=False)
#     for data in data_link:
#         data = data_link.split('\n')
#         city_data = []
#         for address in data:
#             if 'г.' in address:
#                 del address
#             else:
#                 address = address.lstrip() + ', Санкт-Петербург'
#                 city_data.append(address)
#         return city_data
#V0.1
# def data_address(): # Эта функция должна обрабатывать адреса ("Тихоокеанская ул., 10, Санкт-Петербург")
#     link = pd.read_csv(open('data_csv/adress.csv', 'r', encoding='UTF-8'), sep=';')
#     web_link = link[['Адрес заведения']]
#     data_link = web_link.to_string(header=False, index=False)
#     data = data_link.split('\n')
#     city_data = []
#     for address in data:
#         if 'г.' in address:
#             del address
#         else:
#             address = address.lstrip() + ', Санкт-Петербург'
#             city_data.append(address)
#         for all_address in city_data:
#             return all_address

#V0,2
def data_address(): # Эта функция должна обрабатывать адреса ("Тихоокеанская ул., 10, Санкт-Петербург")
    link = pd.read_csv(open("data_csv/adress.csv", 'r', encoding='UTF-8'), sep=';')
    web_link = link.set_index('Название организации').to_dict()['Адрес заведения']
    reverse = defaultdict(list)
    d = []
    for key, value in web_link.items(): #меняет адреса добавляя в конце ' , Санкт-Петербург'.
        if 'г.' in value:
            del value
        else:
            value = value.lstrip() +' , Санкт-Петербург'
            d.append(value)
            patern = '(\S+\s)(\w+\S\D)(\D+)(\d+)(\S+)'
            repl = r'\4\5 \1\2\3'
            text = d 
            number_house = []
            for item in text:  #меняет адреса ставя номер дома спереди.
                if re.match(patern,item):
                    new_number_house = re.sub(patern,repl,item)
                    number_house.append(new_number_house)
                    prospekt = []
                    for prosp in number_house: #меняет адреса заменяет "пр." на "проспект".
                        if 'пр.' in prosp:
                            new_pospekt = re.sub('пр.', 'проспект', prosp)
                            prospekt.append(new_pospekt)
                        else:
                            prospekt.append(prosp)                     
        return prospekt

print(len(data_address()))

#V0.3
# def data_address(): # Эта функция должна обрабатывать адреса ("Тихоокеанская ул., 10, Санкт-Петербург")
#     link = pd.read_csv(open("data_csv/address.csv", 'r', encoding='UTF-8'), sep=';')
#     web_link = link.set_index('Название организации').to_dict()['Адрес заведения']
#     print(len(web_link))
#     reverse = defaultdict(list)
#     d = []
#     for key, value in web_link.items(): #меняет адреса добавляя в конце ' , Санкт-Петербург'.
#         if 'г.' in value:
#             del value
#         else:
#             value = value.lstrip() +' , Санкт-Петербург'
#             d.append(value)
#             patern = '(\S+\s)(\w+\S\D)(\D+)(\d+)(\S+)'
#             repl = r'\4\5 \1\2\3'
#             text = d 
#             number_house = []
#             for item in text:  #меняет адреса ставя номер дома спереди.
#                 if re.match(patern,item):
#                     new_number_house = re.sub(patern,repl,item)
#                     number_house.append(new_number_house)
#                     prospekt = []
#                     for prosp in number_house: #меняет адреса заменяет "пр." на "проспект".
#                         if 'пр.' in prosp:
#                             new_pospekt = re.sub('пр.', 'проспект', prosp)
#                             prospekt.append(new_pospekt)
#                         else:
#                             prospekt.append(prosp)                     
#     return prospekt