salario = float(input('Salário do funcionário: R$'))

if salario > 1250:
    novo_sal = (salario / 100) * 10 + salario
else:
    novo_sal = (salario / 100) * 15 + salario
print('Seu novo salário será R${:.2f}.'.format(novo_sal))
