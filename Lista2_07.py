#Faça um Programa que leia três números e mostre o maior e o menor deles.

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
valor3 = float(input("Digite o terceiro valor: "))

lista = [valor1, valor2, valor3]

print("Menor valor: ", min(lista), "\nMenor valor: ", max(lista))
