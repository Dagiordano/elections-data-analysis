from p1 import export_count_by_local


class ResultsByLocalExporter():
    def __init__(self, data, filename):
        self.data = data
        self.filename = filename
        pass
    
    def export(self):
        
        export_count_by_local(self.data,self.filename)
        return
    
    