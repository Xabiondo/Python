print("metodo cesar")

inputUsuario = str(input("dime una palabra para codificar"))
inputNumero = int(input("dime cuantas letras se va a mover "))
inputUsuario = inputUsuario.lower()

print(ord("a"))
print(ord("z"))

nuevaPalabra = []

for caracter in inputUsuario:
    posicion = ord(caracter)

    if posicion + inputNumero > 122 :
        posicion = posicion - 26 + inputNumero
    else:
        posicion = posicion + inputNumero
    letraUsusario = chr(posicion)
    nuevaPalabra.append(letraUsusario)
        
print(nuevaPalabra)

i = 0 
while i < 50:
    print(i , "elfante, se balanceaba , sobre la tela de una araña, como veia , que no se podria , fueron a llamar a otro elefante ")
    i = i + 1 
     


