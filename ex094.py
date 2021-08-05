pessoa = {}
grupo = []
mulheres = []
acima_media = []
soma_idade = media = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        '''if pessoa['sexo'] == 'F':
            mulheres.append(pessoa['nome'])'''
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma_idade += pessoa['idade']
    grupo.append(pessoa.copy())
    pessoa.clear()
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp not in 'SN':
            print('ERRO! Responda apenas S ou N.')
        else:
            break
    if resp in 'N':
        break
media = soma_idade / len(grupo)
print(grupo)
print('A ', len(grupo))
print(soma_idade)
print('B ', media)
# print('C ', mulheres)
print(f'As mulheres cadastradas foram ', end='')
for i in grupo:
    if i['sexo'] in 'Ff':
        print(f'{i["nome"]}', end='')
print()
print('Lista das pessoas com idade aima da média', end='')
for i in grupo:
    if i['idade'] > media:
        for k, v in i.items():
            print(f'{k} = {v}')

