maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input(f'Peso da {i}ª pessoa: '))

    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'Anterior {anterior}')
print(f'Atual {atual}')
print(f'Maior {maior}')
print(f'Menor {menor}')

'''print(f'O maior peso lido foi de {maior}Kg.')
print(f'O menor peso lido foi de {menor}Kg.')'''