val = []
par = []
impar = []
while True:
    num = (int(input('Digite um valor: ')))
    val.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    resp = str(input('Quer continuar? [S/N] ')).strip().upper().capitalize()
    if resp in 'Nn':
        break
print(f'A lista completa é {val}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')