# Minha solução
n1 = int(input('Digite um número: '))
contd = 0
div = 0
for cont in range(1, n1 + 1):
    div = n1 % cont
    if div % cont == 0:
        contd = contd + 1
    print('[{} % {} = {}<]'.format(n1, cont, div), end=' ')
print(end='\n')
if contd == 2:
    print('O número {} é um número primo.'.format(n1), end=' ')
else:
    print('O número {} náo é primo.'.format(n1), end=' ')
print('Pois o número {} é divisível por {} vezes'.format(n1, contd))
