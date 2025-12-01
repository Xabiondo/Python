def identificadorUnico():
    nombre = str(input("dime tu nombre"))
    dni = str(input("dime tu dni "))
    skip = "x"

    while skip != "":
        skip = str(input("dale a espacio para continuar"))
    while validarDni(dni):
        dni = str(input("dni inválido, repite"))
    
    

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



validarDni("1231J")
