'''
Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
'''

numero = float(input("Digite um número: "))

if(numero // 1 == numero):
    print("numero inteiro")
else:
    print("Numero Decimal")
