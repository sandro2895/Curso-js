import datetime
anosn = int(input('Em que ano o atleta nasceu? '))
datas = datetime.date.today().year
idade = anosn - datas
idade1 = idade * -1
print(idade1)
if idade1 < 10:
    print('O atleta está na categoria MIRIM ')
elif idade1 > 9 and idade1 < 15:
    print('O atleta está na categoria INFANTIL')
elif idade1 > 14 and idade1 < 20:
    print('O atleta está na categoria JUNIOR')
elif idade1 > 19 and idade1 < 26:
    print('O atleta está na categoria SÊNIOR')
elif idade1 > 25:
    print('O atleta está na categoria MASTER')
