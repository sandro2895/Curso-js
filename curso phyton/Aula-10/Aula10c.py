nota1 = float(input('Qual foi a primeira nota? '))
nota2 = float(input('Qual foi a segunda nota? '))
medias = nota1 + nota2
mediad = medias / 2
print('Sua média é: {:.1f}'.format(mediad))
if mediad >= 6.0:
    print('Boa nota você passou!')
else:
    print('Infelizmente você não passou.')
