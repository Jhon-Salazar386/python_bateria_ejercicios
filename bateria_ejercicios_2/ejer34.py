precio = float(input("introduce el precio inicial por kilo: "))
tipo = input("introduce el tipo de uva (a o b): ")
tamaño = int(input("introduce el tamaño (1 o 2): "))
kilos = float(input("introduce los kilos de uva: "))

if tipo == "a":
    if tamaño == 1:
        precio = precio + 0.20
    else:
        precio = precio + 0.30
else:
    if tamaño == 1:
        precio = precio - 0.30
    else:
        precio = precio - 0.50

ganancia = precio * kilos

print("la ganancia obtenida es:", ganancia, "euros")
