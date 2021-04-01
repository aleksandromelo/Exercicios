n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
op = 0

while op != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    op = int(input('>>>>>Qual é a sua opção? '))
    print('=-=' * 10)
    if op == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}.')
    elif op == 2:
        mult = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é {mult}.')
    elif op == 3:
        if n1 > n2:
            print(f'{n1} é maior do que {n2}.')
        elif n2 > n1:
            print(f'{n2} é maior do que {n1}')
        else:
            print(f'{n1} e {n2} são iguais.')
    elif op == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif op == 5:
        print('Fim do programa.')
    else:
        print('Opção inválida. Tente novamente.')
