import os
os.system('cls')
import math

a = int(input('Digite um número: '))
b = int(input('Digite a base que deseja calcular o logaritmo'))

logaritmo = math.log(a,b)
print(f"O logaritmo de {a} na base {b} é {logaritmo}")