mais_18 = 0
tot_h = 0
m_menos20 = 0

while True:
    print(f'-'*35)
    print(f'CADASTER UMA PESSOA')
    print(f'-'*35)

    idade = int(input('Idade: '))
    if idade > 18:
        mais_18 += 1
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        tot_h += 1
    elif sexo == 'F' and idade < 20:
        m_menos20 += 1
    print(f'-'*35)

    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {mais_18}')
print(f'Ao todo temos {tot_h} homens cadastrados.')
print(f'E temos {m_menos20} mulheres com menos de 20 anos.')
