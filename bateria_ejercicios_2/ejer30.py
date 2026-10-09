x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

r1 = float(input("r1: "))
r2 = float(input("r2: "))

d = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)

if d == 0:
    print("Concéntricas")

elif d > r1 + r2:
    print("Exteriores")

elif d == r1 + r2:
    print("Tangentes exteriores")

elif d > abs(r1 - r2):
    print("Secantes")

elif d == abs(r1 - r2):
    print("Tangentes interiores")

else:
    print("Interiores")
