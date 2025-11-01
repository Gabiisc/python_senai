import os
os.system('cls')
import math

#sqrt = raiz
#pow = exponenciação
#diagonal = raiz de altura^2 + base^2

base = int(input("Informe a base do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))

perimetro = (base * 2) + (altura * 2)
area = base * altura

diagonal = math.sqrt((math.pow(base,2)) + (math.pow(altura,2)))

print(base)
print(altura)
print(diagonal)


