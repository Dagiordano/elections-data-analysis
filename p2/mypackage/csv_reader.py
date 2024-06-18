import pandas as pd


class CsvReader:
    def __init__(self, data):
        self.data = data
        pass
    def read_file(self):
        file_csv = pd.read_csv(self.data, on_bad_lines='skip', sep=';')
        diccionario = file_csv.to_dict('records')
        return diccionario
    
    
    