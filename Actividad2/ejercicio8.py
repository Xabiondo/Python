print("ecuación de doble grado")

valor1 = float(input("dime el primer coeficiente"))
valor2 = float(input("dime el segundo coeficiente"))
valor3 = float(input("dime el tercero coeficiente"))


if valor1 == 0 and valor2 == 0 and valor3 == 0:
    print("todos los números son solución ")
    exit()


if valor1 == 0 or valor2 == 0 :
    print("sin solución")
    exit()


primeraSolucion = ((-valor2 + (valor2 ** 2 - (4 * valor1 * valor3))**0.5 )) / (2*valor1)
segundaSolucion = ((-valor2 - (valor2 ** 2 - (4 * valor1 * valor3))**0.5 )) / (2*valor1)


if(primeraSolucion == segundaSolucion):
    print(primeraSolucion)
    exit()

print(primeraSolucion)
print(segundaSolucion)


