cantidad = int(input("¿Cuántos números primos quieres mostrar? "))

contador_primos = 0
numero = 2

while contador_primos < cantidad:

    divisores = 0

    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores += 1

    if divisores == 2:
        print(numero)
        contador_primos += 1

    numero += 1
