def identificadorUnico():
    nombre = str(input("dime tu nombre y apellido"))

    inputUsuario = nombre.split()
    nombre = inputUsuario[0]
    apellido = len(inputUsuario[1])
    dni = str(input("dime tu dni "))
    skip = "x"

    while skip != "":
        skip = str(input("dale a espacio para continuar"))
    while validarDni(dni):
        dni = str(input("dni inválido, repite"))
    print("el dni es válido")
    print("tu identificador es .. " )
    identificador = nombre+str(apellido)+str(dni[0:3])
    print(identificador)
    
    

def validarDni(dni):
    totalLetras = 0
    totalNumeros = 0
    for i in dni:
        if i.isdigit():
            totalNumeros += 1
        elif i.isalpha():
            totalLetras += 1
        if totalLetras == 8 and totalNumeros ==1:
            return True
    return False





identificadorUnico()
