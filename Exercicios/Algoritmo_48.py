import os
os.system('cls')

salario = float(input("Qual o valor do salário mínimo? "))
quilowatts = int(input("Digite a quantidade de quilowatts gasto: "))


salario_um_setimo = salario / 7
valor_um_kw = salario_um_setimo / 100
quilowatts_pago = quilowatts * valor_um_kw
desconto = quilowatts_pago - ((quilowatts_pago / 100) * 10)

print(f"O valor de um kW é R${valor_um_kw}")
print(f"O valor a ser pago é R${quilowatts_pago}")
print(f"O valor com o desconto de 10% é de R${desconto}")
