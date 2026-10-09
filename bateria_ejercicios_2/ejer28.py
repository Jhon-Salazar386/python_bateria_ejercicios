nota = float(input("Ingresa la nota:    "))

edad = int(input("Ingresa la edad:  "))

sexo = input("Ingrese sexo(F/M)")

if(nota >= 5 and edad >= 18 and sexo.lower() == "f"):
    print("Aceptada")
elif(nota >= 5 and edad >= 18 and sexo.lower() == "m"):
    print("Posible")
else:
    print("No aceptado/a")