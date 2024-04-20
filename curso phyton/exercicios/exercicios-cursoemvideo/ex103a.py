def ficha(jog='', gols=0):
    if jog == '' and gols <= 0:
        jog = '<Desconhecido(a)>'
        gols = 0
        return print(f'Jogador(a) {jog} Fez {gols} gol(s) no campeonato.')
    if jog == '' and gols > 0:
        jog = '<Desconhecido(a)>'
        return print(f'Jogador(a) {jog} fez {gols} gols(s) no campeonato.')
    if jog != '' and gols <= 0:
        gols = 0
        return print(f'jogador(a) {jog} fez {gols} gols(s) no campeonato.')
    if jog == '' and gols > 0:
        print(f'jogador(a) {jog} fez {gols} gols(s) no campeonato.')
    else:
        return print(f'Jogador(a) {jog} fez {gols} gols(s) no campeonato.')


N = str(input('Nome de jogador(a): '))
G = str(input('Número de gols: '))
if G.isnumeric():
    G = int(G)
else:
    G = 0

ficha(N, G)
