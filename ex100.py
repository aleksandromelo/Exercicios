numeros = []
def sorteia(lista):
    from time import sleep
    from random import randint
    print(f'Sorteando 5 valores da lista: ', end='')
    for i in range(1, 6):
        s = randint(1, 10)
        lista.append(s)
        print(f'{s} ', end='', flush='')
        sleep(0.3)
    print(' PRONTO!')
    # print(numeros)

def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {lista}, temos {soma}')
    # print(numeros)

sorteia(numeros)
somaPar(numeros)