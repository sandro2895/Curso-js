from random import randint
pc = randint(1, 10)
print('Tente adivinhar um número que estou pensando.')
acertou = False
palpites = 0
while not acertou:
    player = int(input('Qual é seu palpite? '))
    palpites = palpites + 1
    if player == pc:
        acertou = True
    if player > pc:
        print('Errou! Menos')
    if player < pc:
        print('Errou! mais.')
print('Acertou! Foi necessário {} palpite(s)'.format(palpites))
