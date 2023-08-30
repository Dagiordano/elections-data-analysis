from p1 import export_general_results


class GeneralResultsExporter():
    def __init__(self, data, filename):
        self.data = data
        self.filename = filename
        pass
    
    def export(self):
        
        export_general_results(self.data,self.filename)
        return
    