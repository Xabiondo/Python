class Alumno:
    
    def __init__(self, name , nota):
        self.name = name
        self.nota = nota

    def saludar(self):
        print("hola" + name )

    def aprobado(self):
        if self.nota >= 5:
            print("aprobasete")
        else:
            print("no aprobaste ")


xabi = Alumno("xabi" , 10)
xabi.aprobado()




    
    

