n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
if n1 > n2 and n2 > n3:
    print('Maior é {}.'.format(n1))
    print('Menor é {}.'.format(n3))
elif n1 > n2 and n2 < n3 and n1 > n3:
    print('Maior é {}.'.format(n1))
    print('Menor é {}.'.format(n2))




