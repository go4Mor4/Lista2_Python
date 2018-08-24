salario = float(input("Digite o seu salário"))

valor_baixo = salario * 0.20
baixo = salario * 1.20
valor_medio = salario * 0.15
medio = salario * 1.15
valor_alto = salario * 0.10
alto = salario * 1.10
valor_altissimo = salario * 0.05
altissimo = salario * 1.05

print("Antes Reajuste: ", salario)

if salario <= 280:
    print("Aumento: 20%\nValor: ", valor_baixo, "\nFinal: ", baixo)
elif salario > 200 and salario <= 700:
    print("Aumento: 15%\nValor: ", valor_medio, "\nFinal: ", medio)
elif salario > 700 and salario <= 1500:
    print("Aumento: 10%\nValor: ", valor_alto, "\nFinal: ", alto)
else:
    print("Aumento: 5%\nValor: ", valor_altissimo, "\nFinal: ", altissimo)
