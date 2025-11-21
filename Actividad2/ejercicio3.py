print("Comparador de años ")

x = int(input("en que año estamos "))
y = int(input("escribe un año cualquiera "))

if(x < y ):
    print("para llegar al año cualquiera faltan " , y-x )
elif(y < x):
    print("desde el año " , x , " han pasado " , y-x  , " años") 
else:
    print("son iguales ")

