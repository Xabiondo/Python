x = int(input("Escriba el dividendo"))
y = int(input("Escriba el divisor "))

if(y == 0):
    print("el divisor no puede ser 0 ")

cociente = x / y
resto = x % y

if(resto == 0 and  y != 0 ):
    print("la división  es exacta , el resto es  " , resto , "y el cociente es  " , cociente)
else:
    print("la división no es exacta , el resto es " , resto , "y el cociente es  " , cociente)

