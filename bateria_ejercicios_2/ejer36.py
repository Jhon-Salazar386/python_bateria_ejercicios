minutos = int(input("introduce los minutos de la llamada: "))
dia = input("introduce el día: ")
turno = input("introduce el turno (mañana o tarde): ")

if minutos <= 5:
    precio = 1
elif minutos <= 8:
    precio = 1 + (minutos - 5) * 0.80
elif minutos <= 10:
    precio = 1 + 3 * 0.80 + (minutos - 8) * 0.70
else:
    precio = 1 + 3 * 0.80 + 2 * 0.70 + (minutos - 10) * 0.50

if dia == "domingo":
    impuesto = precio * 0.03
elif turno == "mañana":
    impuesto = precio * 0.15
else:
    impuesto = precio * 0.10

total = precio + impuesto

print("precio de la llamada:", precio, "euros")
print("impuesto:", impuesto, "euros")
print("total a pagar:", total, "euros")
