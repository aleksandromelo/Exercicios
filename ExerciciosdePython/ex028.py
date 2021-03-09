from random import randint
print('Pensar em número entre 0 e 5...')
print('=' * 35)
num = int(input('Em que número pensei? '))
pc = randint(0,5)
if num == pc:
    print('Você escolheu {} e eu pensei em {}.'.format(num, pc))
    print('Parabéns! Você acertou!')
else:
    print('Você errou!')




