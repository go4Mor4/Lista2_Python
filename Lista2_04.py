#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ")
vogais = ['a', 'e', 'i', 'o', 'u']

if letra in vogais: print('VOGAL')
else: print('CONSOANTE')
