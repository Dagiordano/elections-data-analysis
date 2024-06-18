import pandas as pd


class GeneralResultsExporter():
    def __init__(self, data, filename):
        self.data = data
        self.filename = filename
        pass
    
    def export(self):
        
        df = pd.DataFrame(self.data)
        resultados = df.groupby('Candidato')['Votos TRICEL'].sum()
        resultados.to_csv(self.filename, sep=';')
        return
    