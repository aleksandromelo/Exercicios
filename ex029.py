v = float(input('Velocidade do veículo: Km'))
if v > 80:
   multa = (v - 80) * 7
   print('Você foi multado em R${:.2f}.'.format(multa))
else:
   print('OK')
