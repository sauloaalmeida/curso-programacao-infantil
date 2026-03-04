import random
import time

tempo = 0.2
fantasma = "👻"

altura = 20
largura = 50

linha = altura // 2
coluna = largura // 2

print("Pressione Ctrl + C para parar...\n")

try:
    while True:

        direcao = random.choice(["cima", "baixo", "esquerda", "direita"])

        if direcao == "cima" and linha > 1:
            linha -= 1
        elif direcao == "baixo" and linha < altura:
            linha += 1
        elif direcao == "esquerda" and coluna > 1:
            coluna -= 1
        elif direcao == "direita" and coluna < largura:
            coluna += 1

        print(f"\033[{linha};{coluna}H" + fantasma )

        time.sleep(tempo)

        print(f"\033[{linha};{coluna}H  ")

except KeyboardInterrupt:
    print("\033[0m")
    print("\nPrograma encerrado!")
