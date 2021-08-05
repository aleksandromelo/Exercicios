from random import sample
print('-'*20)
print('JOGA NA MEGA SENA')
print('-'*20)
n = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {n} JOGOS =-=-=-')
for i in range(1, n+1):
    jogos = sample(range(1, 60), 6)
    print(f'Jogo {i}: {jogos}')


