print("convertidor de distancias ")

cmUsuario = int(input("dime cuantos centrimetos quieres que pase "))
inputUsuario = cmUsuario

km = 0 
m = 0
cm = 0

if cmUsuario > 100000:
    km = cmUsuario // 100000
    cmUsuario = cmUsuario % 100000
if cmUsuario > 100:
    m = cmUsuario // 100
    cmUsuario = cmUsuario % 100
if cmUsuario != 0 :
    cm = cmUsuario 


 
print(inputUsuario , " cm " , "son " , km , "km" , m , "m " , cm , "cm ")
    

    