import csv
import pandas as pd

def import_data():
    file = input('Ingrese nombre del archivo a leer: ')
    file_csv = pd.read_csv(file, on_bad_lines='skip', sep=';')
    diccionario = file_csv.to_dict('records')
    return diccionario 

    