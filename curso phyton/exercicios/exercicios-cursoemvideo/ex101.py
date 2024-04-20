import datetime


def voto(ano=0):
    global idade
    idade = (ano - datetime.date.today().year) * -1
    if 18 <= idade <= 70:
        eleger = f'Com {idade} anos(s): VOTO OBRIGATÓRIO!'
        return eleger
    if 18 > idade > 15:
        eleger = f'Com {idade} anos(s): VOTO OPCIONAL!'
        return eleger
    if idade > 70:
        eleger = f'Com {idade} anos(s): VOTO OPCIONAL!'
        return eleger
    else:
        eleger = f'Com {idade} anos(s) VOTO NEGADO!'
        return eleger


idade = 0
votar = int(input('Em que ano você nasceu? '))
print(f'{voto(votar)}')



