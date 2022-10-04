import pandas as pd

link = pd.read_csv(open('cards.csv', 'r', encoding='UTF-8'), sep=';')
web_link = link[['Ссылка на заведение']]
data_link = web_link.to_string(header=False, index=False)
print(type(data_link))



#    data_link.to_csv('file1.csv', header=False, index=False)

