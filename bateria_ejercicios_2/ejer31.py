a = float(input("introduce el lado a: "))
b = float(input("introduce el lado b: "))
c = float(input("introduce el lado c: "))

if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("triángulo rectángulo")
elif a == b and b == c:
    print("triángulo equilátero")
elif a == b or a == c or b == c:
    print("triángulo isósceles")
else:
    print("triángulo escaleno")
