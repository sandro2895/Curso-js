jogador = {}
jogadores = []
gols = []
total = []
goals2 = []
conta = 0
soma = 0
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).strip()
    partidas = int(input('Quantas partidas? '))
    if partidas > 0:
        for cont in range(0, partidas):
            gols.append(int(input(f'Número de gol(s) na {cont + 1}º partida: ')))
            soma += gols[cont]
    total.append(soma)
    jogador['gol'] = gols[:]
    jogador['total'] = total[:]
    goals2.append(gols[:])
    jogadores.append(jogador.copy())
    gols.clear()
    total.clear()
    soma -= soma
    qs = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while qs not in 'SN':
        qs = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    conta += 1
    if qs == 'N':
        break
print(jogadores)
print('[', '=-=' * 20, ']')
print(f'{"cod"} {"nome"}')

for pos, v in enumerate(jogadores):
    print(f'  {pos:>1} {v["nome"]:<4}   gols(s):{v["gol"]}      Total:{v["total"][0]}')
print('-' * 40)

while True:
    resp = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if resp == 999:
        break
    if resp >= len(jogadores):
        print(f'ERRO! não existe jogador com código {resp}')
    else:
        print(f'------- levantamento de jogador(a) {jogadores[resp]["nome"]}')
        for i, g in enumerate(jogadores[resp]['gol']):
            print(f'     No jogo {i+1} fez {g} gol(s)')
