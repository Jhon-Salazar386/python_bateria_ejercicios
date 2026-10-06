print("Ingresa valores para tupla A")
xa = int(input("valor xa    "))

ya = int(input("valor ya    "))

tupla_A = (xa, ya)

print("Ingresa valores para tupla B")

xb = int(input("valor xb    "))

yb = int(input("valor yb    "))

tupla_B = (xb, yb)

vab = ((tupla_A[0] - tupla_B[0]), (tupla_A[1] - tupla_B[1]))

distancia = abs(((vab[0]**2) + (vab[1]**2)) **0.5)

print(vab)

print(tupla_A[1])

print(distancia)