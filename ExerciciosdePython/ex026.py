f = str(input('Diite uma frase: ')).strip().upper()
print('A letra A apareceu {} vezes na frase.'.format(f.count('A')))
print('Primeira posição {}'.format(f.find('A')+1))
print('Última posição {}'.format(f.rfind('A')+1))


