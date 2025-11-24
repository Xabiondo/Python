print("calculo de áreas , eliga una figura")

print("Triángulo ")
print("Círculo")
print("que figura quiere calcular (Escribe T o C )")

decisionUsuario = str(input("escribe"))

if decisionUsuario == "T":
    base = int(input ("escribe la base"))
    altura = int(input("escrible la altura"))
    areaTriangulo = base * altura / 2 
    print("un triangulo con base " , base , " y altura " , altura , "tiene " , areaTriangulo , " area ")

if decisionUsuario =="C":
    radio = int(input ( "dime el radio del circulo "))
    areaCirculo = radio * 3.141592 
    print("un circulo de radio " , radio , " tiene un area de  " , areaCirculo)


