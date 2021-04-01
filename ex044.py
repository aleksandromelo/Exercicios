preco = float(input('Valor da compra: R$'))

print('''FORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque(10% desconto)
[ 2 ] À vista cartão(5% desconto)
[ 3 ] 2 x cartão
[ 4 ] 3 x cartão(20% juros)''')

pag = int(input('Qual a forma de pagamento? '))

if pag == 1 :
    total = preco - (preco / 100 * 10)
elif pag == 2:
    total = preco - (preco / 100 * 5)
elif pag == 3:
    total = preco
    parc = preco / 2
    print('Você pagará 2 parcelas de R${:.2f} cada uma.'.format(parc))
elif pag == 4:
    total = preco + (preco / 100 * 20)
    parc = total / 3
    print('Você pagará 3 parcelas de R${:.2f} cada uma.'.format(parc))
else:
    total = 0
    print('Opção inválida. Tente novamente.')
print('Total de R${:.2f}'.format(total))