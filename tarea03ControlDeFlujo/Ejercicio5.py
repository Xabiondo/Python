nombre1 = str(input("dime un nombre"))
nombre2 = str(input("dime otro nombre"))
print(len(nombre1))

if nombre1[0] == nombre2[0]:
    print("empiezan por la misma letra !!")
elif nombre2[len()] == nombre1[0]:
    print("terminan por la misma letra !! ")
else:
    print("no hay coincidencia")