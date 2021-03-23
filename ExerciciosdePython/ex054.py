from datetime import date
ano_atual = date.today().year
maior = 0
menor = 0
for i in range(1, 8):
    ano_nasc = int(input(f'Em que ano a {i}ª nasceu? '))
    if ano_atual - ano_nasc >= 18:
        maior += 1
    else:
        menor += 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade.')
print(f'E também tivemos {menor} pessoas menores de idade.')