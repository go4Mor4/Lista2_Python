#Faça um Programa que leia três números e mostre o maior deles.

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

valores = [valor1, valor2, valor3]

print(f'O maior número é {max(valores)}')
