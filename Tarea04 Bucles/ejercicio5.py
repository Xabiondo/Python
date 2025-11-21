frase = str(input("dime una frase"))
letra = str(input("dime una letra"))
contador = 0
indice = len(frase)
print(frase[0] , letra)


for caracter in frase:
    if caracter == letra:
        contador = contador + 1

print(contador)
