s = float(input('Qual o salário do funcionário? R$'))
novo = s + (s * 15 / 100)
print('Um funcionário que ganhava {:.2f}, com 15% de aumento, passa a receber {:.2f}'.format(s, novo))
