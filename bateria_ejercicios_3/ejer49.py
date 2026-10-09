numero_real = float(input("Ingresa un numero: "))

numero_exponente = int(input("Ingresa el numero"))

potencia = 1

if(numero_exponente > 0):
    for i in range(numero_exponente):
        potencia *= numero_real
        print(potencia)

    print("Potencia = ", potencia)
elif(numero_exponente == 0):
    print("Resultado = ", 1)
