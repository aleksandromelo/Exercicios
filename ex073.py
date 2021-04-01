times = ('Flamengo', 'Palmeiras', 'Atlético MG', 'Santos', 'Gremio',
         'São Paulo', 'Fluminense', 'Corinthians', 'Chapecoense', 'Vasco', 'Botafogo')

print(f'Os 5 primeiros são {times[0:5]}')
print(f'Os 4 últimos  são {times[-4:]}')
print(f'Times em ordem alfabética {sorted(times)}')
# colocacao =
print(f'A Chapecoense está na {times.index("Chapecoense") + 1}ª posição.')