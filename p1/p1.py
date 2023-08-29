
import pandas as pd
import csv

def import_data():
    file = input('Ingrese nombre del archivo a leer: ')
    file_csv = pd.read_csv(file, on_bad_lines='skip', sep=';')
    diccionario = file_csv.to_dict('records')
    return diccionario



file = 'data.csv'

a= pd.read_csv(file, on_bad_lines='skip', sep=';')
dic= a.to_dict('records')



df = pd.DataFrame(dic)

prob = df['Distrito']


ciudades = df['Región'].value_counts()
