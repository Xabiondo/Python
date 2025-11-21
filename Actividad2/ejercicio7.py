primerNumero = float(input("dime el valor del primer coeficiente"))
segundoNumero = float(input("dime el valor del segundo coeficiente"))

solucion = -segundoNumero / primerNumero


if primerNumero == 0:
    print("no hay solución ")
    exit()
if primerNumero and segundoNumero == 0:
    print("son todos solución ")
    exit()
print(solucion)