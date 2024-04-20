cas = float(input('Qual é o valor da casa? '))
sal = float(input('Quanto você ganha de salario? '))
anospg = int(input('Em quantos anos pretende pagar? '))
anosd = anospg * 12
pres = cas / anosd
sal2 = sal * 30/100
print(anosd)
print(sal2)
print(pres)

if pres > sal2:
    print('Infelizmente seu empréstimo não foi aceito. pois 30% do seu salario que é: {:.2f}R$. não é maior ou igual '
          'a prestação mensal da casa que é: {:.2f}R$'.format(sal2, pres))
else:
    print('Parabens seu empréstimo foi aprovado!')
