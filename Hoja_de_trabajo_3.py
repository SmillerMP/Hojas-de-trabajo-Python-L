
#EJERCICIO 1
numero = input("Ingrese un numero: ")
numero = int(numero)

i = 1
while i <= numero:
    print("*"*i)
    i += 1

print("")
print("-----")
print("")

#EJERCICIO 2
numero = input("Ingrese un numero entero positivo: ")
numero = int(numero)

if numero < 0:
    print ("Error, el numero debe ser positivo")
else:
    i = 0
    while i <= numero:
        print (numero, ", ",end="")
        numero -= 1

print("")
print("")
print("-----")
print("")

#EJERCICIO 3
numero = input("Ingresa un numero entero: ")
numero = int(numero)

i = 2
while numero % i != 0:
    i += 1
if i == numero:
    print (numero, "es primo")
else:
    print (numero, "no es un numero primo")