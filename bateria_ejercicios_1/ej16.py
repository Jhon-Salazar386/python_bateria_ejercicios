distancia = float(input("Introduce la distancia entre los coches"))

velocidad1 = float(input("Ingresa velocidad de coche 1"))

velocidad2 = float(input("Ingresa velocidad de coche 2"))

tiempo = distancia / (velocidad1 - velocidad2)

minutos = tiempo * 60

print("El coche 1 alcanzara al coche 2 en ", minutos, " minutos ")