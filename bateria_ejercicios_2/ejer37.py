numero = int(input("introduce el número del dado: "))

if numero < 1 or numero > 6:
    print("error: número incorrecto.")
elif numero == 1:
    print("seis")
elif numero == 2:
    print("cinco")
elif numero == 3:
    print("cuatro")
elif numero == 4:
    print("tres")
elif numero == 5:
    print("dos")
else:
    print("uno")
