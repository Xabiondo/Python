def diaSemana(numeroDia):
    numeroDia = numeroDia % 7 
    #ESto lo hago para que siempre sea menor que 7 , si sale 0 es domingo, que solo sale cuando debe de ser domingo
    
    match numeroDia:
        case 1:
            print("es lunes")
        case 2:
            print("es martes")
        case 3:
            print("es miercoles")
        case 4:
            print("es jueves")
        case 5:
            print("es viernes")
        case 6:
            print("es sábado")
        case _:
            print("es domingo")

diaSemana(8)


            
