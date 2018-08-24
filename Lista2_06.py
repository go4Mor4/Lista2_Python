valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

if valor1 > valor2 and valor1 > valor3:
    print("O número ", valor1, " é o maior")

elif valor2 > valor1 and valor2 > valor3:
    print("O número ", valor2, " é o maior")

elif valor3 > valor1 and valor3 > valor2:
    print("O número ", valor3, " é o maior")

else:
    print("Os maiores números são iguais")
