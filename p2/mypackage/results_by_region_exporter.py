import pandas as pd

class ResultsByLocalExporter():
    def __init__(self, data, filename):
        self.data = data
        self.filename = filename
        pass
    
    def export(self):
        
        df = pd.DataFrame(self.data)
        local_usuario = input("Ingrese nombre del local: ")
        local_df = df[df['Local']== local_usuario]
        conteo_por_local = local_df.groupby('Candidato')['Votos TRICEL'].sum()
        conteo_por_local.to_csv(self.filename, sep=';')
        return
    