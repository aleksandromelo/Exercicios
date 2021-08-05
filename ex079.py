listnum = []
while True:
    num = int(input('Digite um valor: '))

    if num not in listnum:
        listnum.append(num)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar.')

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()

    # ord_cesc = sorted(listnum)

    if resp in 'Nn':
        break
listnum.sort()
print(listnum)