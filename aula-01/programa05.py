import random
import time

tempo = 1
olhos_abertos = "@@"
olhos_fechados = "--"

cores = [
    "\033[91m",  # vermelho
    "\033[92m",  # verde
    "\033[93m",  # amarelo
    "\033[94m",  # azul
    "\033[95m",  # roxo
    "\033[96m"   # ciano
]

preto = "\033[30m"

print("Pressione Ctrl + C para parar...\n")

try:
    while True:
        linha = random.randint(3, 20)
        coluna = random.randint(1, 50)
        cor = random.choice(cores)

        print(f"\033[{linha};{coluna}H" + cor + olhos_abertos)

        time.sleep(tempo)

        print(f"\033[{linha};{coluna}H  " + preto)

        print(f"\033[{linha};{coluna}H" + cor + olhos_fechados)

        time.sleep(tempo/5)
        
        print(f"\033[{linha};{coluna}H  " + preto)


except KeyboardInterrupt:
    print("\033[0m")
    print("\nPrograma encerrado!")
