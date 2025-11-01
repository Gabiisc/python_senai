import os
os.system('cls')
from datetime import datetime

hora_relogio = int(input("Informe a hora do seu relógio: ").replace(":",""))
hora_atual = int(datetime.now().strftime("%H%M"))

if hora_relogio == hora_atual:
    print("Seu relógio está correto.")

elif hora_relogio > hora_atual:
    dif_hora = hora_relogio - hora_atual
    print(f"Seu relógio está adiantado em {dif_hora} minutos.")

else:
    dif_hora = hora_atual - hora_relogio
    print(f"Seu relógio está atrasado em {dif_hora} minutos.")