import os
os.system('cls')

nota01 = float(input("Digite a primeira nota: "))
nota02 = float(input("Digite a segunda note: "))
nota03 = float(input("Digite a terceira nota: "))
nota04 = float(input("Digite a quarta nota: "))

media = (nota01 + nota02 + nota03 + nota04) / 4

if media >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")