fras1 = input('Digite uma frase: ')
fras2 = fras1.replace(' ', '')
fras3 = fras2.upper()

if fras3 == fras3[::-1]:
    print('Essa frase é um palíndromo')
    print('Pois {} é igual a {}. A mesma frase invertida'.format(fras3, fras3[::-1]))
else:
    print('essa frase não é um palíndromo')
    print('Pois {} não é igual a {}. A mesma frase invertida'.format(fras3, fras3[::-1]))



