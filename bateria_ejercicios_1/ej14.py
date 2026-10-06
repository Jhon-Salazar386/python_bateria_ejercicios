numero = int(input("Introduce un numero de 2 cifras"))

decena = numero // 10

unidad = numero % 10

num_invertido = unidad * 10 + decena

print(num_invertido)