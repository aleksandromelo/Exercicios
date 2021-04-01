from random import randint

pc = randint(0, 10)
print('Sou seu computador...Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpite = 0

while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpite += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais...Tente mais uma vez.')
        elif jogador > pc:
            print('Menos...Tente mais uma vez.')

print(f'Acertou com {palpite} tentativas. Parabéns!')
