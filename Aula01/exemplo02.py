import os #Identifica o SO 
os.system('cls') #Executa o comando cls do prompt de comando do Windows, que limpa a tela do terminal.

'''
Tipos de dados:
stg = string
int = inteiros 1, 2, 3
float = numeros reais, flutuantes 1.2, 1.3, 1.4
bool = True ou False
'''

nome = 'Senai'
numero = 25
valor = 3.8
prg = True

print(type(nome))
print(type(numero))
print(type(valor))
print(type(prg))

# Todo input é automaticamente str a menos que seja convertido, no exemplo abaixo, sempre cairá no else
aleatoria = (input("Digite um valor: "))
print(f"O tipo do dado informado é: ", type(aleatoria))
print()

if type(aleatoria) == int:
    print("Valor válido")
else:
    print("Valor inválido, digite um número")

# Conversão do tipo de dado, neste exemplo, se for digitado qualquer coisa que não seja um inteiro, dará erro
print()
aleatoria = int(input("Digite um valor: "))
print(type(aleatoria))

if type(aleatoria) == int:
    print("Valor válido")
else:
    print("Valor inválido, digite um número")