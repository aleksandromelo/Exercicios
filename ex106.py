while True:
    resp = str(input('Função ou Biblioteca > ')).upper()
    print(help(resp))
    if resp == 'FIM':
        print('ATÉ LOGO')
        break