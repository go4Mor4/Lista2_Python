#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Digite seu sexo [F, M]: ")

if sexo == 'F' or sexo == 'f': print("Seu sexo é Feminino")
elif sexo == 'M' or sexo == 'm': print("Seu sexo é Masculino")
else: print("Sexo Inválido")
