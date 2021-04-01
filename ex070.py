print(f'-'*35)
print(f'LOJA SUPER BARATÃO')
print(f'-'*35)

tot = 0
prod_1000 = 0
cont = 0
menor = ''
custo = 0

while True:
    nome_prod = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))

    cont += 1
    tot += preco

    if cont == 1 or preco < custo:
        custo = preco
        menor = nome_prod

    if preco > 1000:
        prod_1000 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N':
        break

print(f'FIM DO PROGRAMA')
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {prod_1000} produtos custando mais de R$1000.00.')
print(f'O produto mais barato foi {menor} que custa R${custo:.2f}')
