soma = 0
cont = 0
for i in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você digitou {} números pares e a soma foi: {}'.format(cont, soma))