lado1 = float(input("Lado 1: "))
lado2 = float(input("Lado 2: "))
lado3 = float(input("Lado 3: "))

if lado1 + lado2 > lado3 or lado1 + lado3 > lado2 or lado2 + lado3 > lado1:
    print("É UM TRINGULO")
    if lado1 == lado2 and lado1 == lado3:
        print("Equilatero")
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print("Isóceles")
    else:
        print("Escaleno")
else:
    print("Não é um TRINGULO")
