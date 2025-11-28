try: 
    numero1 = int(input("dime un número"))
    numero2 = int(input("dime otro número"))
except ValueError:
    print("pon numeros")

if numero2 == 0:
    raise Exception("el segundo número no puede ser 0 ")

print("suma" , numero1 + numero2)
print("resta" , numero1 - numero2)
print("producto" , numero1 * numero2)
print("division " , numero1 / numero2)


