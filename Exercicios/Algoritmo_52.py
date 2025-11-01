import os
os.system('cls')
import math

lado_quadrado = int(input("Informe o lado do quadrado: "))

perimetro = lado_quadrado * lado_quadrado
area = lado_quadrado * 4
raiz = math.sqrt(2)
diagonal = lado_quadrado * raiz
diagonal = round(diagonal, 2)

print(f"O perimetro do quadrado é: {perimetro}")
print(f"A área do quadrado é: {area}")
print(f"A diagonal do quadrado é: {diagonal}")