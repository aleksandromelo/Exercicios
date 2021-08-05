from time import sleep
def maior(*args):
    print('Analisando os valores passados...')
    '''print(f'{str(args)} Foram informados {len(args)} valores ao todo.')
    print(f'O maior valor passado foi {max(args)}')'''#Esse código usa as próprias funções do Python.
    cont = m = 0
    for v in args:
        print(f'{v} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            m = v
        else:
            if v > m:
                m = v
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {m}.')

maior(2, 9, 4, 5, 7, 1)