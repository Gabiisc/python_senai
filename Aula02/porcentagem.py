import os
os.system('cls')

quantidade = int(input("Digite uma quantidade: "))
valor = int(input("Digite o valor: "))
desconto = int(input("Desconto aplicado: "))

valor_final = quantidade * (valor - ((valor / 100) * desconto))

print(f"O valor final é: R$ {valor_final}")





