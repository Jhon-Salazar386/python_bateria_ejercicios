factorial = int(input("Ingrese valor de numero 1"))

contador = 1

resultado = 1

while(contador <= factorial):

    resultado *= contador
    contador = contador + 1


print(resultado)

""""

factorial = int(input("Ingrese valor de numero 1"))

contador = 1

resultado = 1

for i in range(contador, factorial + 1):
    resultado *= contador
    contador = contador + 1


print(resultado)

"""
