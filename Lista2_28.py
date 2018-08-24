tipo_carne = input("Digite o tipo da carne que irá comprar: ")
quantidade_carne = int(input("Digite a quantidade de carne que irá comprar: "))
tipo_pagamento = input("Escreva o tipo de tipo de pagamento: ")

print("Tipo de carne:", tipo_carne, "\nQuantidade de carne:", quantidade_carne)

preco_file_duplo1 = quantidade_carne * 4.90
preco_file_duplo2 = quantidade_carne * 5.80

alcatra1 = quantidade_carne * 5.90
alcatra2 = quantidade_carne * 6.80

picanha1 = quantidade_carne * 6.90
picanha2 = quantidade_carne * 7.80

if tipo_carne == 'filé duplo':
    if quantidade_carne > 5:
        preco_total = preco_file_duplo1
    else:
        preco_total = preco_file_duplo2
elif tipo_carne == 'alcatra':
    if quantidade_carne > 5:
        preco_total = alcatra1
    else:
        preco_total = alcatra2
elif tipo_carne == 'picanha':
    if quantidade_carne > 5:
        preco_total = picanha1
    else:
        preco_total = picanha2
else:
    print("Carne Invalida")

if tipo_pagamento == 'Cartão Tabajara':
    desconto = preco_total * 0.05
    print("Tipo de pagamento: ", tipo_pagamento)
    print("Valor do desconto: ", desconto)
    print("Valor Final: ", (preco_total - desconto))
else:
    print("Tipo de pagamento: normal\nValor do desocnto: 0")
    print("Valor Final: ", preco_total)
