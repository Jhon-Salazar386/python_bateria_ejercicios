correctas = int(input("Ingresa numero de respuestas correctas "))
incorrectas = int(input("Ingresa numero de respuestas incorrectas "))
blanco = int(input("Ingresa numero de respuestas en blanco "))

calificacion = (correctas * 5) + (incorrectas * -1) + (blanco * 0)

print("Correctas =", correctas, " incorrectas =", incorrectas, " en blanco =", blanco)
print("Resultado = ", calificacion)