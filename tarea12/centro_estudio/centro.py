import sys
import os


ruta_padre = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ruta_padre)

from alumno.alumno import *

class Centro_estudio:
    def __init__(self ):
        self.centro = "4v"

    def imprimirAlumno(self):
        introducir_datos_alumno()

centro = Centro_estudio()

print(centro.centro)
centro.imprimirAlumno()
        

    
        




        
    
