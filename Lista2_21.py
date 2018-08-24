import math
saque = int(input("Valor para sacar: "))
nota100 = saque / 100
nota100_certo = math.floor(nota100)
resto_nota_100 = (nota100 - nota100_certo) * 100

nota50 = resto_nota_100 / 50
nota50_certo = math.floor(nota50)
resto_nota_50 = (nota50 - nota50_certo) * 50

nota10 = resto_nota_50 / 10
nota10_certo = math.floor(nota10)
resto_nota_10 = (nota10 - nota10_certo) * 10

nota5 = resto_nota_10 / 5
nota5_certo = math.floor(nota5)
nota1 = (nota5 - nota5_certo) * 5

print("Notas 100: ", nota100_certo, "\nNotas50: ", nota50_certo, "\nNota 10: ", nota10_certo, "\nNota 1: ", round(nota1))
