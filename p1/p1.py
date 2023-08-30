
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
    num_ciudades_df = pd.DataFrame(num_ciudades)
    opciones_mesa=4
    num_ciudades_df['Región'] = num_ciudades_df['Región'].apply(lambda x: x/opciones_mesa)
    num_ciudades_df.to_csv(filename, sep=';')
    return


def export_general_results(data,filename):
    df = pd.DataFrame(data)
    resultados = df.groupby('Candidato')['Votos TRICEL'].sum()
    resultados.to_csv(filename, sep=';')
    return


def export_count_by_local(data,filename):
    df = pd.DataFrame(data)
    local_usuario = input("Ingrese nombre del local: ")
    local_df = df[df['Local']== local_usuario]
    conteo_por_local = local_df.groupby('Candidato')['Votos Tricel'].sum()
    conteo_por_local.to_csv(filename, sep=';')
    return
    
    
