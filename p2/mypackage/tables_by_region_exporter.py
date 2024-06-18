
import pandas as pd


class TablesByRegionExporter():
    def __init__(self, data, filename):
        self.data = data
        self.filename = filename
        pass
    
    def export(self):
        
        df = pd.DataFrame(self.data)
        num_ciudades = df['Región'].value_counts()
        num_ciudades_df = pd.DataFrame(num_ciudades)
        opciones_mesa=4
        num_ciudades_df['Región'] = num_ciudades_df['Región'].apply(lambda x: x/opciones_mesa)
        num_ciudades_df.to_csv(self.filename, sep=';')
        return
        return
    