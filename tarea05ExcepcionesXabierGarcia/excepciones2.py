
try:
    fichero = open("fichero.txt" , "w")
    try:
        fichero.write("hola")
    except:
        print("algo ha ido mal, igual no esta creado")
    finally:
        fichero.close()
except:
    print("algo ha ido mal ")
