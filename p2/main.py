
from mypackage.parse_options import ParseOptions
from mypackage.csv_reader import CsvReader
from mypackage.tables_by_region_exporter import TablesByRegionExporter
from mypackage.general_results_exporter import GeneralResultsExporter
from mypackage.results_by_region_exporter import ResultsByLocalExporter

class Main(ParseOptions, CsvReader, TablesByRegionExporter, GeneralResultsExporter, ResultsByLocalExporter):
    def __init__(self):
        pass
    
    def main(self):
        opcion=0
        while opcion !=5:
            print("\n")
            ParseOptions.display_menu()      
            opcion=ParseOptions.get_option()
            print(opcion)
            
            #leer archivo
            if opcion == '1':
                archivo = input("Ingrese nombre del archivo: ")
                read = CsvReader(archivo)
                dic=read.read_file()
                
            #mesas por region
            elif opcion=='2':
                filename = input("\n Ingrese nombre del archivo de salida: ")
                
                mesa=TablesByRegionExporter(dic,filename)
                mesa.export()
                
            #recuento general
            elif opcion == '3':
                filename2 = input("\n Ingrese nombre del archivo de salida: ")
                
                general=GeneralResultsExporter(dic,filename2)
                general.export()
                
            elif opcion == '4':
                filename3 = input("\n Ingrese nombre del archivo de salida: ")
                
                local=ResultsByLocalExporter(dic,filename3)
                local.export()
            else:
                pass
            
                
                
            
                
        
        
        
        return
    
    

        
        
main_obj = Main()


main_obj.main()