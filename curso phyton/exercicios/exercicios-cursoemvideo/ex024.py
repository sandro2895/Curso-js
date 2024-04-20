cid = (input('Qual o nome da cidade? '))
tit = cid.title()
tit2 = tit.strip()
test = tit2[:5] == 'Santo' in tit2
print('-Se sua cidade tem Santo no começo do nome? a resposta é: {}'.format(test))


