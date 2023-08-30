from ..p1.py import export_general_results


class general():
    def __init__(self, data, filename):
        self.data = data
        self.filename = filename
        pass
    
    def export(self):
        
        export_general_results(self.data,self.filename)
        return
    