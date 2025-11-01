import os
os.system('cls')

bem_vindo = input("Para efetuar seu cadastro em nossa plataforma, aperte enter.")
nome = (input("Insira seu nome: "))
endereco = (input("Endereço: "))
telefone = (int(input(("Digite seu telefone (somente números): "))))

print(f'Olá {nome}, seja bem vindo! \nOs dados informados foram: \nEndereço: {endereco}\nTelefone {telefone}')