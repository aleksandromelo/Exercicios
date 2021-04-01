n = int(input('Digite um valor para calcular seu fatorial: '))
f = 1
print(f'Calculando {n}! = ', end =' ')

for i in range(1, n+1):
    print(f'{n}', end = ' ')
    print(' x ' if n > 1 else ' = ', end = ' ')
    f *= i
    n -= 1

print(f)