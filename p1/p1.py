
import pandas as pd
import csv

file = 'data.csv'

a= pd.read_csv(file, on_bad_lines='skip', sep=';')
dic= a.to_dict('records')



df = pd.DataFrame(dic)

prob = df['Distrito']


ciudades = df['Región'].value_counts()
