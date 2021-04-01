num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
par = 0
print(f'Você digitou os valores: {num}')
if 9 in num:
    print(f'O valor 9 apareceu {num.count(9)} vezes.')
else:
    print(f'O valor 9 não foi digitado')
if 3 in num :
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição.')
else:
    print(f'O valor 3 não foi digitado.')
for i in num:
    if i % 2 == 0:
        par += 1
print(f'Os valores pares digitados foram {par}')
