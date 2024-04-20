num = 0
while True:
    print('-'*20)
    num = int(input('Qual número você quer ver a tabuada? '))
    if num < 0:
        break
    for cont in range(1, 10 + 1):
        mult = num * cont
        print(f'{num} x {cont} = {mult}')
