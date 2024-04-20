idade = int(input('Qual é a sua idade? '))
if idade < 13:
    print('Você é uma criança!')
elif 13 <= idade <= 19:
    print('Você é um adolescente!')
else:
    print('Você é um adulto!')
