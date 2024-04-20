num = ('zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
       'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
       'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis',
       'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    quest = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {num[quest]}')
    perg = ''
    perg = str(input('Quer continuar? ')).strip().upper()[0]
    while perg not in 'SN':
        perg = str(input('Quer continuar? ')).strip().upper()[0]
    if perg == 'N':
        break
