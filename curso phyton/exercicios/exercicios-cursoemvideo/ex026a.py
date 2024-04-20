frase1 = str(input('Digite uma frase: '))
frase2 = frase1.strip()
frase3 = frase1.upper()
conta1 = frase3.count('A')
conta2 = frase3.find('A')+1
conta3 = frase3.rfind('A')
print('Nessa frase a letra A aparece um total de: {} Vezes '.format(conta1))
print('Nessa frase a primeira aparição da letra A é na posição: {}'.format(conta2))
print('Nessa frase a letra A aparece por ultimo na posição: {}'.format(conta3))
