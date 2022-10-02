import csv

def all_web():
    with open('cards.csv', 'r', encoding='UTF-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            return(row['Ссылка на заведение'])