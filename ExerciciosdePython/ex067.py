while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print(f'-' * 35)
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')
    print(f'-' * 35)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
