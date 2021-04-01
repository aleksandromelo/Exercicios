'''Programa clássico sobre média de notas de um aluno'''

n1 = float(input('Prineira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2)/ 2

print('Sua média foi: {}'.format(media))

if media < 5.0:
    print('Você está reprovado.')
elif media >= 7.0:
    print("Você está aprovado. Parabéns!")
else:
    print('Você está de recuperação.')