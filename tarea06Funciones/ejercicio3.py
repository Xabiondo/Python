def esPrimo(numero ):
    numeroDivisores = 0 
    for i in range (1 ,  numero+1):
        if numero % i == 0:
            numeroDivisores = numeroDivisores + 1 
    if numeroDivisores == 2 :
        return True
    
    return False

if(esPrimo(10)):
    print("es primo")
else:
    print("no es primo")
    