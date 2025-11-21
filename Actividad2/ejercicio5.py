print("comparador de tres numeros ")
numero1 = int(input("dime un número"))
numero2 = int(input("dime otro número"))
numero3 = int(input("dime el ultimo  número"))


if(numero3 == numero1 == numero3):
    print("los tres números son iguales")
elif(numero1 == numero2 or numero2 == numero3 or numero1 == numero3):
    print("has puesto dos número iguales")
else:
    print("son todos diferentes ")