pessoa = []
grupo = []
maior = menor = 0
while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(grupo) == 0:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    grupo.append(pessoa[:])
    pessoa.clear()

    resp = str(input('Quer continuar? [S/N] ')).strip().upper().capitalize()
    if resp in 'Nn':
        break
print('-='*35)
print(f'Ao todo, você cadastrou {len(grupo)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for i in grupo:
    if i[1] == maior:
        print(f'{i[0]} ', end='')
print()
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for i in grupo:
    if i[1] == menor:
        print(f'{i[0]} ', end='')