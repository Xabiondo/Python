x = int(input("dime un valor "))
y = int(input("dime otro valor "))

class Calculadora:
    def __init__(self , x , y ):
        self.x = x 
        self.y = y 

    def suma(self):
        print(self.x + self.y)

    def resta(self):
        print(self.x - self.y)

    def multiplicacion(self):
        print(self.x * self.y)

    def division(self):
        print(self.x / self.y)

calculadora = Calculadora(x , y )
calculadora.suma()
calculadora.resta()
calculadora.multiplicacion()
calculadora.division()

        