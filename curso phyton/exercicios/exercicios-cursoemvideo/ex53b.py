fras1 = input('Digite uma frase: ')
palavrs = fras1.split()
juntar = ''.join(palavrs)
inverso = ''
for letras in range(len(juntar)-1, -1, -1):
    inverso = inverso + (juntar[letras])
print(juntar, inverso)
