#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


horario = input("Digite [M, V, N]: ").upper()

if horario == 'M': print("Bom Dia")
elif horario == 'V': print("Boa Tarde")
elif horario == 'N': print("Boa Noite")
else: print("Valor Inválido")
