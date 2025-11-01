import os
os.system('cls')

texto = "SeNaI frederICO JacÓ"

print(texto.upper()) #Deixa tudo maiúsculo
print(texto.lower()) #Deixa tudo minúsculo

texto_alterado = texto.replace("jacó", "Jacob")
print(texto_alterado)
print(texto_alterado.upper())


print(texto[::-1]) #printa o texto de trás para frente