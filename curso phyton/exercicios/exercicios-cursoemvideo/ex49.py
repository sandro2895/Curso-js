mult = int(input('Qual número você quer saber a tabuada? '))
for cont in range(1, 10 + 1):
    mulc = mult * cont
    print('{} x {} = {}'.format(mult, cont, mulc))
