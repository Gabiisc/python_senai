import os
os.system('cls')

idade = int(input("Digite sua idade: "))

if idade <= 11:
    print("Grupo pertencente: Infantil")
elif idade >= 12 and idade <= 17:
    print("Grupo pertencente: Adolescente")
elif idade >= 18 and idade <= 25:
    print("Grupo pertencente: Jovem")
else:
    print("Grupo pertencente: Adulto")