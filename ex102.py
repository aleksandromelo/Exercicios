def fatorial(f, show=False):
    '''
    ->Calcula o Fatorial de um número.
    :param f: o número a ser calculado.
    :param show: (Opcional) Mostra ou não a conta.
    :return: Retorna o fatorial de um número n.
    '''
    print()
    print('-'*35)
    n = 1
    for c in range(f, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print('x', end='')
            else:
                print('=', end='')
        n *= c
    return f'{n}'


print(fatorial(3, show=True))
help(fatorial)
