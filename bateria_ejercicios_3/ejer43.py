numero = -1
suma = 0
contar_numeros = 0

while numero != 0:
    
    numero = int(input("Ingresa un numero diferente de 0: "))

    if(numero != 0):
        suma += numero
        contar_numeros += 1

media = suma / contar_numeros

print("Suma: ",suma)
print("Media: ", media)

"""

suma = 0
contar_numeros = 0

while True:
    numero = int(input("Ingresa un numero diferente de 0: "))

    if(numero == 0):
        break

    suma += numero
    contar_numeros += 1

media = suma / contar_numeros

print("Suma: ",suma)
print("Media: ", media)

"""
