print("calculadora de bisiestos")

año = int(input("dime un año para ver si es bisiesto"))

bool = True

if(año % 100 == 0 ):
    bool = False

if(año % 400 == 0 ):
    bool = True

if(año % 4 == 0 and bool  ):
    print("el año es bisiesto")
else:
    print("el año no es bisiesto")