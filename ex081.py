num = []

while True:
    num.append(int(input('Digite um valor: ')))

    resp = str(input('Quer continuar? [S/N] ')).strip().upper().capitalize()

    if resp in 'Nn':
        break

print(f'Você digitou {len(num)} elementos.')
print(f'Os valores em ordem decrescente são: {sorted(num, reverse=True)}')
# print(f'Os valores em ordem decrescente são: {num.sort(reverse=True)}') uma opção ao código acima
if 5 in num:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')