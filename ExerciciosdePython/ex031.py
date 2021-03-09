distancia = float(input('Qual é a distância da sua viagem? '))
if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45

print('Você está prestes a começar uma viagem de {}km.'.format(distancia))
print('E o preço de sua passagem será de R${:.2f}'.format(passagem))