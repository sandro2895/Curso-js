
#c = -1
#while c < 10:
   #c = c + 1
    #print(c)

#c = 11
#while c > 0:
   # c = c  -1
    #print(c)

c = 1
par = 0
impar = 0

while c != 0:
    c = int(input('Digite um número: '))
    if c != 0:
        if c % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print('Tem o total de {} pares.'.format(par))
print('Tem o total de {} impares.'.format(impar))

