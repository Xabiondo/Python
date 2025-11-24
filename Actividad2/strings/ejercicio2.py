frase = str(input("dime una frase "))
letraUsuario = str(input("dime una letra "))
fraseMayus = frase.upper()  
fraseMinus = frase.lower() 

letraMasAlta = 0 
letraMasBaja = 0 

contiene = False 

for x in frase:
    if ord(x) > letraMasAlta:
        letraMasAlta = ord(x)

    if ord(x) < letraMasBaja:
        letraMasBaja = ord(x)

letraMasAlta = chr(letraMasAlta)
letraMasBaja = chr(letraMasBaja)
print(frase) 
print(fraseMayus)
print(fraseMinus)
print("letra mas alta ", letraMasAlta )
print("letra mas baja ", letraMasBaja )
if letraUsuario in frase:
    print("la letra si que esta en la frase ")
else: 
    print("la letra no esta en la frase")

