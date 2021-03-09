va = float(input('Valor da casa R$'))
sc = float(input('Salário do comprador R$'))
anos = int(input('Em quantos anos irá pagar? '))

prestacao = va / (anos * 12)

print('A prestação será de R${:.2f}.'.format(prestacao))

if prestacao > sc * 30 / 100:
    print('Empréstimo negado!')
else:
    print('Empréstimo concedido.')
