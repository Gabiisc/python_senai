import os
os.system('cls')

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
divisao = a / b
resto = a % b

print(f'O dividendo desta operação é: {a} ')
print(f'O divisor : {b}')
print(f'O quociente é: {divisao}')
print(f'O resto da divisão de {a} / {b} é: {resto}')