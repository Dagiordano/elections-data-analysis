
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




def export_tables_by_region(data,filename):
    df = pd.DataFrame(data)
    num_ciudades = df['Región'].value_counts()
    num_ciudades_df = df.DataFrame(num_ciudades)
    num_ciudades_df.to_csv('mesas_por_region.csv', sep=';')
    return
    
