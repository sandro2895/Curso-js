sal = float(input('Qual voce recebe de salário? '))
salt = 0
salal1 = sal * 10 / 100
salal2 = sal * 15 / 100
if sal > 1250.00:
    salt = sal + salal1
if sal <= 1250.00:
    salt = sal + salal2
print('O seu salario é de: {:.2f}R$. Então você vai passar a receber: {:.2f}R$'.format(sal, salt))
