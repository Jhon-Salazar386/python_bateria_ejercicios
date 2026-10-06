
def calcular_perimetro(base, altura):

    print(2 * (base + altura))

def calcular_area(base, altura):

    print(base * altura)

base: float = float(input("Ingresa base"))

altura: float = float(input("Ingresa altura"))

calcular_perimetro(base, altura)

calcular_area(base, altura)