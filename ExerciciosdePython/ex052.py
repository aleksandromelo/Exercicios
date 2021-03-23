n = int(input('Digite um número: '))
cont = 0
for i in range(1, n+1):
    div = n % i
    if div == 0:
        cont += 1
if cont == 2:
    print('{} é um número primo.'.format(n))
else:
    print('{} não é um número primo.'.format(n))
print(cont)