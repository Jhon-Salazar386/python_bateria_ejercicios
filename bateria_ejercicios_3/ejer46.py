num1 = int(input("Ingresa rango inicial "))
num2 = int(input("Ingresa rango final "))

for i in range(num1, num2 + 1):

    if(i % 2 == 0):
        print(i, " es numero par ")
