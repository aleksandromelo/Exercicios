soma = 0
valores = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        valores += 1
        soma += i
print(valores)
print(soma)