valores = []
maior =  0
menor = 0
for i in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {i}: ')))

    if i == 0:
        maior = menor = valores[i]
    elif i != 0 and valores[i] >= maior:
        maior = valores[i]
    elif i != 0 and valores[i] <= menor:
        menor = valores[i]

print(valores)
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, j in enumerate(valores):
    if j == maior:
        print(f'{i}...', end='')
print()

print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, j in enumerate(valores):
    if j == menor:
        print(f'{i}...', end='')