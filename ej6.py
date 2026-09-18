num_numeros = int(input("Cuantos numeros quieres agregar"))
suma = 0

for i in range(num_numeros):
    numero = int(input("Agrega valor al numero " + str(i + 1)))
    suma += numero

print(suma / num_numeros)