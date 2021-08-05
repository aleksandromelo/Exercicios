palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO')
for i in palavras:
    print(f'\nNa palavra {i} temos: ', end='')
    for j in i:
        if j.lower() in 'aeiou':
            print(j, end=' ')



