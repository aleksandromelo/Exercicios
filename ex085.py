valor = [[], []]
for i in range(1, 8):
    n = int(input(f'Digite o {i}º valor: '))
    if n % 2 == 0:
        valor[0].append(n)
    else:
        valor[1].append(n)
print('-='*35)
print(valor)
valor[0].sort()
valor[1].sort()
print(f'Os valores pares digitados foram: {valor[0]}')
print(f'Os valores ímpares digitados foram: {valor[1]}')