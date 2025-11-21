contraseña = "contraseña"

contraseñaUsuario = str(input("introduce la contraseña "))

while contraseña != contraseñaUsuario:
    contraseñaUsuario = str(input("te equivocate, otra vez "))

print("muy bien !! lo conseguiste")