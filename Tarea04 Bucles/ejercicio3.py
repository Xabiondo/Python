numeroEntero = int(input("dime un número entero positivo"))

numerosImpares = []
contador = 0 

while numeroEntero > contador:
    contador = contador + 1 
    if contador % 2 == 1:
        numerosImpares.append(contador)

print(numerosImpares)