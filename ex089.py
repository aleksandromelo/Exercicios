turma = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2)/2
    turma.append([nome, [n1, n2], media])
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp in 'Nn':
        break
print('-='*35)
print(f'{"No.":<4}{"NOME":<10}{"MÈDIA":>8}')
print('-'*25)
for i, a in enumerate(turma):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')


