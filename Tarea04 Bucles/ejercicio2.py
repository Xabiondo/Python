edad = int(input("dime tu edad"))

if edad > 19:
    raise Exception("lo siento , no edades por encima de 19 ")

for i in range(20 - edad):
    print("tu edad ahora es " , edad)
    edad = edad + 1

