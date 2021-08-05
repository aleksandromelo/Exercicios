def voto(a):
    from datetime import date
    idade = date.today().year - ano
    if idade >= 18 and idade <= 65:
        return f'Com {idade} anos: VOTO OBRIGÁTORIO.'
    elif idade < 18 and idade >= 16 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: NÃO VOTA.'


ano = int(input('Em que ano você nasceu? '))
print(voto(ano))