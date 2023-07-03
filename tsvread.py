import pandas as pd
import pyarrow


def read_tsv(filename):
    fields = ['Герои', "O"]
    with open(filename, encoding='utf-8') as file:
        data = pd.read_table(file, sep='\t', usecols=[1, 2])
    print(data)


read_tsvo = read_tsv('dev_ru.tsv')
