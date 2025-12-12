
class Ordenador:
    def __init__(self , discoDuro = True , corriente = True) :
        self.discoDuro = discoDuro  
        self.corriente = corriente

    def getDiscoDuro(self):
        return self.discoDuro
    
    def setDiscoDuro(self , x):
        self.discoDuro = x 

    def getCorriente(self):
        return self.corriente 
    
    def setCorriente(self , x ):
        self.corriente = x 

    def funcionaDiscoDuro(self):
        if(self.discoDuro):
            print("funciona el disco duro")
        else:
            print("no funciona ")
    
    def hayCorriente(self):
        if(self.corriente):
            print("hay corriente")
        else:
            print("no hay corriente")
            
ordenata = Ordenador(True , False)
ordenata.funcionaDiscoDuro()
ordenata.hayCorriente()





       