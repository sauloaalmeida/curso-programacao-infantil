idade = int(input("Quantos anos você tem? "))
fezAniversario = input("Você já fez aniversário esse ano? (Digite apenas S ou N) ")

ano_atual = 2026

if(fezAniversario == "N" or fezAniversario == "n"):
    ano_atual = ano_atual - 1

ano_nascimento = ano_atual - idade

print("Você nasceu no ano de: ", ano_nascimento)
