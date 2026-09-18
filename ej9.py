num_articulos = int(input("numero de articulos adquiridos"))
total_sin_descuento = 0

for i in range(num_articulos):
    valor_articulo = int(input("Valor del producto " + str(i + 1)))
    total_sin_descuento += valor_articulo

descuento = (total_sin_descuento * 15) / 100

total_con_descuento = total_sin_descuento - descuento

print(descuento)
print(total_con_descuento)