#Faça um Programa que peça dois números e imprima o maior deles.

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

if n1 > n2: print("O maior número é ", n1)
elif n2 > n1: print("O maior número é ", n2)
else: print("Os números são iguais")
