
peso = input("Ingresa tu peso en Kg: " )
estatura = input("Ingresa tu estatura en metros: ")

imc = round(float(peso)/float(estatura)**2,2)

print ("Su Indice de Masa Corpotal (IMC) es: ",imc)
