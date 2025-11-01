import os
os.system('cls')
import math

angulo = float(input(f'Insira o angulo em graus: '))
graus = math.radians(angulo)

seno = math.sin(graus)
cosseno = math.cos(graus)
tangente = math.tan(graus)
secante = 1 / seno
cossecante = 1 / cosseno
cotangente = 1 / tangente

print(f"Seno: {seno}")
print(f"Cosseno: {cosseno}")
print(f"Tangente: {tangente}")
print(f"Secante: {secante}")
print(f"Cossecante: {cossecante}")
print(f"Cotangente: {cotangente}")