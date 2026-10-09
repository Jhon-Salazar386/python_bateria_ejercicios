suma = 0
fuera_intervalo = 0
igual_intervalo = 0

while True:

    limite_superior = int(input("Ingresa el limite superior: "))
    limite_inferior = int(input("Ingresa limite inferior: "))

    if(limite_superior < limite_inferior):
        print("Limite superior no puede ser menor al limite inferior")
        continue

    while True:

        numero = int(input("Ingresa numero dentro del intervalo: "))

        if(numero == 0):
            break
        else:
            if(numero < limite_superior and numero > limite_inferior):

                suma += numero

            elif(numero == limite_superior or numero == limite_inferior):
                igual_intervalo += 1

            else:
                fuera_intervalo += 1
    break

print("Resultado de la suma: ", suma)
print("Numeros iguales a uno de los limiter: ", igual_intervalo)
print("Numeros fueras del intervalo: ", fuera_intervalo)
        
