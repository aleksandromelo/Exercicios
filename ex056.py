cont_idade = 0
menos_20 = 0
mais_velho = 0

for i in range(1, 5):
    print(f'----- {i}ª Pessoa -----')
    nome = str(input('Nome: ')).upper()
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).upper()

    if sexo == 'F' and idade < 20:
        menos_20 += 1

    if sexo == 'M' and idade > mais_velho:
        mais_velho = idade
        nome_mais_velho = nome

    cont_idade += idade
    media = cont_idade / 4

print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {mais_velho} anos e se chama {nome_mais_velho}.')
print(f'Ao todo são {menos_20} mulheres com menos de 20 anos.')