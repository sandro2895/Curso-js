jogador = {'nome': str(input('Nome do jogador: ')), 'gols': [0]}
gols = []
soma = 0
partidas = int(input('Quantas partidas? '))
if partidas > 0:
    for cont in range(0, partidas):
        gols.append(int(input(f'Quantos gol(s) na {cont+1}º partida? ')))
        jogador['gols'] = gols[:]
        soma = soma + gols[cont]
else:
    jogador['gols'] = [0]
jogador['total'] = soma
print('[', '=-=' * 25, ']')
print(jogador)
print('[', '=-=' * 25, ']')
print('        ||', '---' * 15, '||')
print('[', '=-=' * 25, ']')
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('[', '=-=' * 25, ']')
print('        ||', '---' * 15, '||')
print('[', '=-=' * 25, ']')
print(f'O jogador {jogador["nome"]} jogou {partidas} partida(s).')
for pos, cont in enumerate(gols):
    print(f'=> Na partida {pos+1}, fez {cont} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
print('[', '=-=' * 25, ']')
