print("metodo cesar")

inputUsuario = str(input("dime una palabra para codificar"))


print(ord("a"))

nuevaPalabra = []

for caracter in inputUsuario:
    if(caracter == "z"):
        letra = chr(98)
    if(caracter == "y"):
        letra = chr(97)

    else:
        posicion = ord(caracter ) + 2 
        letra = chr(posicion)
    nuevaPalabra.append(letra)
print(nuevaPalabra)
     




