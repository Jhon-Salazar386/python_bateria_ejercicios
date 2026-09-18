sueldo_base = float(input("Ingresa el sueldo base: "))

venta1 = float(input("Ingresa el valor de la primera venta: "))
venta2 = float(input("Ingresa el valor de la segunda venta: "))
venta3 = float(input("Ingresa el valor de la tercera venta: "))

total_ventas = venta1 + venta2 + venta3

comision = total_ventas * 0.10

total_mes = sueldo_base + comision

print("Comisión por las tres ventas:" + str(comision))
print("Total que recibirá en el mes:" + str(total_mes))
