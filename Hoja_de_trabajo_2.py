#EJERCICIO 1

contra = "Holapython"

acceso = input("Ingresa la contraseña: ")
acceso = acceso.capitalize()

if contra == acceso:
    print ("     contrasena correcta, BIENVENIDO")
else:
    print ("     contrasena incorrecta")


print("-----------")
print("-----------")
print("-----------")

#EJERCICIO 2
sexo = input("Ingrese su sexo (femenino o masculino): ")
nombre = input("Ingrese su nombre: ")

nombre = nombre.capitalize()
letra = nombre[0]
sexo = sexo.capitalize()

letras1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M"]
letras2 = ["N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


def grupoa():
    print (nombre, "de sexo:", sexo, "esta en el Grupo: A")

def grupob():
    print (nombre, "de sexo:", sexo, "esta en el Grupo: B")

if sexo == "Femenino":
    for x in letras1:
        if x == letra:
            grupoa()
            exit()

    for x in letras2:
        if x == letra:
            grupob()
            exit()

elif sexo == "Masculino":
    for x in letras2:
        if x == letra:
            grupoa()
            exit()

    for x in letras1:
        if x == letra:
            grupob()
            exit()
else:
    print("Asegurese que no hay error en la escritura de femenino o masculino")

        

