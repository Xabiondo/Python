from abc import ABC , abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    
    def __init__(self , rueda , color):
        self.rueda = rueda 
        self.color = color
        
        
class Coche(Vehiculo):
    def __init__(self ,rueda, color,  velocidad , cilindrada ):
        super().__init__(rueda , color)
        self.velocidad = velocidad 
        self.cilindrada = cilindrada 


class Camioneta(Coche):
    def __init__(self, velocidad, cilindrada ,  carga , rueda , color):
        super().__init__(velocidad, cilindrada , rueda , color )
        self.carga = carga 

class Bicicleta(Vehiculo):
    def __init__(self, rueda, color , tipo):
        super().__init__(rueda, color)
        self.tipo = tipo 

class Motocicleta(Bicicleta):
    def __init__(self, rueda, color, tipo ,velocidad , cilindrada ):
        super().__init__(rueda, color, tipo)
        self.cilindrada = cilindrada 
        self.velocidad  = velocidad

def catalogar(arrayVehiculos):
    for vehiculo in arrayVehiculos:
       print(vehiculo.__class__.__name__)
       print("cantidad de ruedas : " , vehiculo.rueda)
       print("color  del vehiculo  : " , vehiculo.color)

def catalogarPersonalizado(arrayVehiculos , x = None):
    if x == None:
        print("envía un número de ruedas")
        return

    y = 0 
    for vehiculo in arrayVehiculos:
        if(vehiculo.rueda == x):
            print(vehiculo.__class__.__name__)
            print("cantidad de ruedas : " , vehiculo.rueda)
            print("color  del vehiculo  : " , vehiculo.color)
            y = y+1
    print("se han encontrado " , y , "vehiculos con este número de ruedas " , x)





bici = Bicicleta(3 ,"rojo" , "montaña")

vehiculos = [bici]

catalogar(vehiculos)
catalogarPersonalizado(vehiculos , 3)







        