import math
numero = int(input("Digite um número menor ou igual a 1000: "))
if numero <= 1000:
    centena = numero / 100
    centena2 = math.floor(float(centena))
    resto_centena = centena - centena2
    resto_multiplicado = resto_centena * 100

    dezena = resto_multiplicado / 10
    dezena2 = math.floor(float(dezena))
    unidade = dezena - dezena2
    unidade_certo = unidade * 10

    print("Centena(s): ", centena2)
    print("dezena(s): ", dezena2)
    print("Unidade(s): ", round(unidade_certo))

else:
    print("VOCÊ DIGITOU UM NÚMERO MAIOR QUE 1000")
