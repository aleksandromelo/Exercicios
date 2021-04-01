from random import randint
print(f'-=-'*10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print(f'-=-'*10)
cont = 0

while True:
    n = int(input('Digite um valor: '))
    op = ''
    while op not in 'PI':
        op = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'-'*35)

    pc = randint(0, 11)

    soma = n + pc

    if soma % 2 == 0:
        print(f'Você jogou {n} e o computador jogou {pc}. Total de {soma} DEU PAR')
        resp = 'P'
    else:
        print(f'Você jogou {n} e o computador jogou {pc}. Total de {soma} DEU ÍMPAR')
        resp = 'I'
    print(f'-' * 35)
    if op == resp:
        print('Você VENCEU!')
        print('Vamos continuar jogando...')
        print(f'-=-' * 10)
        cont += 1
    else:
        print('Você PERDEU!')
        print(f'-=-' * 10)
        print(f'GAME OVER! Você venceu {cont} vezes.')
        break
