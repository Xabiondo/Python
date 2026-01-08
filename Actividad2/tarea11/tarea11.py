class Fecha:
    def __init__(self , dia , mes , año):
        self.dia = dia 
        self.mes =  mes
        self.año = año

    @property
    def dia(self):
        return self._dia
    
    @dia.setter
    def dia(self , x):
        if x > 31 or x < 1:
            self._dia = 1
            return
            
        self._dia = x 
    
    @property
    def mes(self):
        return self._mes
    
    @mes.setter
    def mes(self , x ):
        if x > 12 or x < 1 :
            self._mes = 1 
            return
        self._mes = x

    @property
    def año(self):
        return self._año
    @año.setter
    def año(self  , x) :
        self._año = x 
fecha = Fecha( 1 , 13 , 1)



    





        