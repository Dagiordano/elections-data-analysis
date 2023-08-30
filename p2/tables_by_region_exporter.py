from ..p1.py import export_tables_by_region


class tabla():
    def __init__(self, data, filename):
        self.data = data
        self.filename = filename
        pass
    
    def export(self):
        
        export_tables_by_region(self.data,self.filename)
        return
    