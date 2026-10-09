numero = int(input("Ingresa un numero:    "))

potencia = int(input("Ingresa numero de potencia:   "))

if(potencia == 0):
    print("El resultado es 1")
elif(potencia < 0):
    print(numero ** (1 / potencia))
else:
    print("El resultado es = ", numero ** potencia)