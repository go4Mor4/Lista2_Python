'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
'''

morangos = int(input("Digite a quantidade de morangos [kg]: "))
macas = int(input("Digite a quantidade de maças [kg]: "))
preco_morango1 = morangos * 2.50
preco_morango2 = morangos * 2.20

preco_maca1 = macas * 1.80
preco_maca2 = macas * 1.50

print("quantidade de maçãs: ", macas, "\nQuantidade de morangos: ", morangos)

if morangos > 5:
    preco_certo_morango = preco_morango1
else:
    preco_certo_morango = preco_morango2

if macas > 5:
    preco_certo_maca = preco_maca1
else:
    preco_certo_maca = preco_maca2

preco_total = preco_certo_maca + preco_certo_morango

if preco_total > 25 or (macas + morangos) > 8:
    print("Preço final: ", (preco_total - (preco_total * 0.1)))
else:
    print("Preço final: ", preco_total)
