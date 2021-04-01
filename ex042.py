'''O programa verifica e informa de acordo com os seguimentos informados
   qual o tipo do triângulo.
'''

s1 = int(input('Primeiro seguimento: '))
s2 = int(input('Segundo seguimento: '))
s3 = int(input('Terceiro seguimento: '))

if s1 > s2 + s3 or s2 > s1 + s3 or s3 > s1 + s2:
    print('Estes seguimentos não podem formar um triângulo.')
elif s1 == s2 == s3:
    print('Todos os lados iguais: EQUILÁTERO')
elif s1 != s2 != s3 and s1 != s3:
    print('Todos os lados diferentes: ESCALENO')
elif s1 == s2 or s1 == s3 or s2 == s3:
    print('Dois lados iguais: ISÓSCELES')

