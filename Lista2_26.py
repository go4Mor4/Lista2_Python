'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''

litros = int(input("Digite a quantidade de litros: "))
combustivel = input("Digite o tipo do combustivel [G, A]: ")

preco_alcool1 = (1.90 * 0.03)
preco_alcool2 = (1.90 * 0.05)
preco_gasolina1 = (2.50 * 0.04)
preco_gasolina2 = (2.50 * 0.06)

print("Litros Vendidos: ", litros)

if combustivel == 'a' or combustivel == 'A':
    print("Combustivel: alcool")
    if litros <= 20:
        desconto = (1.90 - preco_alcool1) * litros
        print("Preço: ", desconto)
    else:
        desconto = (1.90 - preco_alcool2) * litros
        print("Preço: ", desconto)
elif combustivel == 'g' or combustivel == 'G':
    print("Combustivel: gasolina")
    if litros <= 20:
        desconto = (2.50 - preco_gasolina1) * litros
        print("Preço: ", desconto)
    else:
        desconto = (2.50 - preco_gasolina2) * litros
        print("Preço: ", desconto)
else:
    print("Valor Invalido")
