frase = str(input("dime una frase "))
cantidadLetras = len(frase)
print("tiene  " , cantidadLetras , "  letras ")

numUsuario = int(input("dime un numero"))

if numUsuario <= cantidadLetras:
    letraDerecha = frase[numUsuario -1 ]
    letraIzquierda = frase[cantidadLetras - numUsuario]
    print("desde el inicio " , letraDerecha)
    print("desde el final  " , letraIzquierda)

if cantidadLetras > 3 :
    primeras3 = frase[:3]
    ultimas3 = frase[-3:]
    print("las primeras " , primeras3)
    print("ultimas 3 " , ultimas3)


for x in frase :
    print(x)