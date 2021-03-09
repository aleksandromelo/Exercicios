p = float(input('Qual o preço do produto? R$'))
porc = (p / 100) * 5
desc = p - porc
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}.'.format(p, desc))
