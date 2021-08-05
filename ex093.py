jogador = {}
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
partidas = []
for i in range(0, tot):
    partidas.append(int(input(f'Quantos gols na partida {i}? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 35)
print(jogador)
print('-=' * 35)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 35)
print(f'O jogador {jogador["nome"]} jogou {tot} partidas.')
# for i in range(0, tot):
for i, v in enumerate(jogador['gols']):
    print(f'  => Na partida {i}, fez {v} gols')
