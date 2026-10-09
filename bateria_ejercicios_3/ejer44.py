mayor_cero = 0
menor_cero = 0
igual_cero = 0

contador = int(input("Ingresa el numero de valores que quieres agregar: "))
if(contador > 0):
    for i in range(contador):
        numero = int(input("Ingresa valor a ser comparado: "))

        if(numero > 0):
            mayor_cero += 1
        elif(numero < 0):
            menor_cero += 1
        else:
            igual_cero += 1

    print("Mayor a cero: ",mayor_cero)
    print("Menor a cero: ",menor_cero)
    print("Igual a cero: ",igual_cero)
    
else:
    print("El contador no puede ser 0")
