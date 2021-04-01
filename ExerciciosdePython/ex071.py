valor = int(input('Qual valor você quer sacar? R$'))

cinquenta = int(valor / 50)
valor = valor - (cinquenta*50)

vinte = int(valor / 20)
valor = valor - (vinte*20)

dez = int(valor / 10)
valor = valor - (dez*10)

um = int(valor / 1)
valor = valor - (um*1)

if cinquenta > 0:
    print(f'Total de {cinquenta} cédulas de R$50,00')
elif vinte > 0:
    print(f'Total de {vinte} cédulas de R$20,00')
elif dez > 0:
    print(f'Total de {dez} cédulas de R$10,00')
elif um > 0:
    print(f'Total de {um} cédulas de R$1,00')



'''print(cinquenta)
print(valor)
print(vinte)
print(dez)
print(um)'''

