aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
print('-='*35)
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['média']<= 5:
    aluno['situação'] = 'Reprovado'
else:
    aluno['situação'] = 'Recuperação'
for k,v in aluno.items():
    print(f'- {k} é igual a {v}.')
