c = 0
v = []
ultimo = 0
anterior = 0
atual = 0

while c < 6:
    n = int(input('Digite um valor: '))
    if c == 0:
        v.append(n)
        ultimo = n
        print('Adicionado ao final da lista...')
        if c == 1 and n < ultimo:
            anterior = n
            v.insert(0, anterior)
        else:
            v.append(n)
            anterior = ultimo
            ultimo = n

    c += 1