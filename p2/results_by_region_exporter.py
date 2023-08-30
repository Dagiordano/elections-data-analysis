from ..p1.py import export_count_by_local


class local():
    def __init__(self, data, filename):
        self.data = data
        self.filename = filename
        pass
    
    def export(self):
        
        export_count_by_local(self.data,self.filename)
        return
    
    