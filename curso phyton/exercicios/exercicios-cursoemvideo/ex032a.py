import datetime
ano = int(input('Digite um número de ano para eu saber se é bissexto.'
                ' Se digitar o número 0 eu mostro o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de: {} é bissexto'.format(ano))

else:
    print('O ano de: {} não é bissexto'.format(ano))
