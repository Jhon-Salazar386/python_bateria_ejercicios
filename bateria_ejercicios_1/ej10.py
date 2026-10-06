parcial1 = float(input("INgresa la nota del parcial 1"))
parcial2 = float(input("INgresa la nota del parcial 2"))
parcial3 = float(input("INgresa la nota del parcial 3"))

examen = float(input("Ingresa nota del examen final"))

trabajo = float(input("Ingresa nota del trabajo"))

promedio_parciales = (parcial1 + parcial2 + parcial3) / 3

calificacion = (promedio_parciales * 0.55) + (examen * 0.30) + (trabajo * 0.15)
print("La calificacion final es = ", calificacion)