jogador = {}
partidas = []
time = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for i in range(1, tot + 1):
        partidas.append(int(input(f'Quantos gols na partida {i}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    partidas.clear()
    time.append(jogador.copy())
    resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resp in 'N':
        break
print(time)
print('-=' * 35)
# print(f'{"cod":<4}{"nome":<8}{"gols":^10}{"total":>10}')
# print('-' * 35)
for k, v in enumerate(time):
    print(f'{k:>4} ', end='')
    for i in v.values():
        print(f'{str(i):<15}', end='')
    print()
print('-'*40)


