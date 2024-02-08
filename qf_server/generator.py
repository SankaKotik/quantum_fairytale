# Программа генерирует квантовую сказку из нескольких предложений.
# Данные автоматически подтягиваются из csv-таблицы рядом с файлом.
#
# https://absurdopedia.net/wiki/Абсурдотека:Квантовая_сказка


import csv
import random

def generator (digit):
    current = 0
    for i in range (digit):
        current = current * 2 + random.getrandbits(1)
        yield current

def mk_qft (data):
    yield (data[0][0])
    
    for sentence, chooser in enumerate (generator (7), start=1):
        yield (data[(64 // (2 ** (sentence - 1)))*chooser][sentence])

def load_data (csv_location):
    with open (csv_location) as csvfile:
        return list (csv.reader (csvfile, delimiter=','))
