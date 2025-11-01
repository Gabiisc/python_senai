import os
os.system('cls')

nome = input("Nome: ")
nome_completo = nome
primeiro_caracter = nome[0]
ultimo_caracter = nome[-1]
tres_primeiros = nome[0:3]
quarto_caracter = nome[3]
exceto_primeiro = nome[1::]
dois_ultimos = nome[-2::]

print(f"Nome completo: {nome_completo}")
print(f"Primeira letra: {primeiro_caracter}")
print(f"Última letra: {ultimo_caracter}")
print(f"Três primeiras letras: {tres_primeiros}")
print(f"Quarto caracter: {quarto_caracter}")
print(f"Exceto primeiro: {exceto_primeiro}")
print(f"Dois últimos: {dois_ultimos}")

