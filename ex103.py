def ficha(nome='<desconhecido>', gol=0):
    print()
    print('-'*35)
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')

n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)

# ficha(n, g)