from datetime import datetime
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de Nascimento: '))
pessoa['idade'] = datetime.now().year - ano_nasc
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['salário'] = int(input('Salário: '))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratação'] + 35) - datetime.now().year)
for k, v in pessoa.items():
    print(f'- {k} tem o valor {v}.')