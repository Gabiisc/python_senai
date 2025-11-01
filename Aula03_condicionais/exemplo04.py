import os
os.system('cls')

altura = float(input("Digite sua altura: "))
idade = int(input("Digite sua idade: "))

valida_altura = altura == 1.70
valida_idade = idade == 16

if valida_altura and valida_idade:
    print("Modelo aprovada! 😄")

elif not valida_altura and valida_idade:
    print("Altura reprovada, idade ok.")

elif valida_altura and not valida_idade:
    print("Altura ok, idade reprovada.")

else:
    print("Modelo reprovada! 😞")
