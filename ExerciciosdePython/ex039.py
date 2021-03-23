'''Alistamento militar
   O programa informa conforme a idade se o individuo já está no ano de alistamento ou,
   se idade inferior a 18 anos, quantos anos faltam para o alistamento ou ainda,
   se idade superior a 18 anos, há quantos anos deveria ter se alistado.
'''
from datetime import date

ano_nasc = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
ano_falta = 18 - idade
ano_atrasado = idade - 18

if idade == 18:
    print('Parabéns! Você tem {} anos e já pode se alistar.'.format(idade))
elif idade < 18:
    print('Voê tem {} anos e ainda faltam {} anos para o seu alistamento.'.format(idade, ano_falta))
else:
    print('Você tem {} anos e deveria ter se alistado há {} anos atrás.'.format(idade, ano_atrasado))
