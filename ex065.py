n = 0
op = ''
cont = 0
soma = 0
maior = 0
menor = 0

while  op in 'Ss':
    n = int(input('Digite um número: '))
    op = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    cont += 1
    soma += n
    media = soma / cont

    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n

        if n < menor:
             menor = n

print(f'{cont}, {media}')
print(f'{maior}, {menor}')
