print("introduce un día con el formato --> día/DD/MM")

usuario = str(input("escribelo "))

inputUsuario = usuario.split("/")
inputUsuario[1] = int(inputUsuario[1])
inputUsuario[2] = int(inputUsuario[2])


if  not (inputUsuario[0] == "lunes" or inputUsuario[0] == "martes" or inputUsuario[0] == "miercoles" or inputUsuario[0] == "jueves" or inputUsuario[0] == "viernes"):
    print("el dia no es valido")
    exit()

if inputUsuario[1] > 31 or inputUsuario[1] < 0:
    print("el día numérico esta mal")
    exit()

if inputUsuario[2] > 12 or inputUsuario[2] < 0:
    print("el mes es erróneo ")
    exit()


if inputUsuario[0] == "lunes" or inputUsuario[0] == "martes" or inputUsuario[0] == "miercoles":
    print("dime si hubo examenes")
    respuesta = str(input("escribe , si o no "))
    if respuesta == "si":
        aprobados = int(input("cuantos han aprobado"))
        suspendidos = int(input("cuantos han suspendido"))
        totalAlumnos = aprobados + suspendidos 
        porcentajeAprobados = aprobados  * 100/ totalAlumnos

        print("el total de aprobados es de " , porcentajeAprobados , " %")

if inputUsuario[0] == "jueves":
    totalAsistencia = int(input("escribe el porcentaje de gente que ha asistido (Ejemplo 45)"))
    if totalAsistencia >= 50:
        print("asistio la mayoría")
    else:
        print("no asisitio la mayoría ")

if inputUsuario[1] == 1 and( inputUsuario[2] == 1 or inputUsuario[2] == 7):
    print("comienzo del nuevo ciclo ")
    cantidadAlumnos = int(input("cuantos alumnos hay "))
    precio = int(input("dime cuanto vale cada matricula "))

    cantidadIngresada = precio * cantidadAlumnos 
    print("has ganado " , cantidadIngresada)


    

