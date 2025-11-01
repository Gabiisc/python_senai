import os
os.system('cls')

nome = 'Senai'

print(len(nome)) #quantidade de posições
print(nome[1]) #segunda letra
print(nome[4]) #última letra

print(nome[1:4]) #da segunda até a 3 letra, a última [4] não é printada, para nela antes do print

print(nome[::2]) #printa a primeira posição, pula 1 posição, printa a próxima posição...  SeNaI - printa SNI
print(nome[::3]) #printa a primeira posição, pula 2 posições, printa a póxima... SenA - printa SA

print(nome[2::]) #comeca a printar a partir da posição 2... seNAI - printa SAI

print(nome[:3]) #printa desde o inicio e para na posição 3, sem printá-la... SENai - printa SEN

print(nome[3:]) #pula as três primeiras posições e printa todas as outras... senAI - prita ai
print(nome[::-1]) #printa o texto de trás para frente.. ianeS