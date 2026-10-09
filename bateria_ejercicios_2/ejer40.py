peso = float(input("introduce el peso del paquete en kg: "))
zona = int(input("introduce la zona de destino (1-5): "))

if peso <= 0:
    print("error: el peso debe ser mayor que 0.")
elif zona < 1 or zona > 5:
    print("error: la zona debe estar entre 1 y 5.")
else:
    if zona == 1:
        precio = 24
    elif zona == 2:
        precio = 20
    elif zona == 3:
        precio = 21
    elif zona == 4:
        precio = 10
    else:
        precio = 18

    coste = peso * precio

    print("el coste total del envío es:", coste, "euros")
