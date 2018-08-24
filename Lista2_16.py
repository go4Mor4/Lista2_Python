import math
a = float(input("Digite A: "))
if a == 0:
    print("Valor Invalido")
else:
    b = float(input("Digite B: "))
    c = float(input("Digite C: "))

delta = (b ** 2) - (4 * a * c)

if delta < 0:
        print("A equação não possui raizes reais")
else:
    x1 = (-b + math.sqrt(delta)) / 2 * a
    x2 = (-b - math.sqrt(delta)) / 2 * a
if delta == 0:
        print("1 Raiz real: ", x1)
else:
        print("2 raizes reais, x1: ", x1, "\nx2: ", x2)
