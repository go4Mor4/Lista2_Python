#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


horario = input("Digite [M, V, N]: ")

if horario == 'M' or horario == 'm':
    print("Bom Dia")
elif horario == 'V' or horario == 'v':
    print("Boa Tarde")
elif horario == 'N' or horario == 'n':
    print("Boa Noite")
else:
    print("Valor Inválido")
