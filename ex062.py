n = int(input('Quantos termos você quer ver? '))
c = 2
anterior = 0
proximo = 1
print(f'{anterior} -> {proximo} ->', end='')

while c < n:
    atual = anterior + proximo
    print(f'{atual} -> ', end='')
    anterior = proximo
    proximo = atual

    c += 1
print(' FIM')