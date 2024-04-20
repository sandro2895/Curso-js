#test = '\033[7:34:41m Ola mundo!\033[m'
#print(test)
n1 = 5
n2 = 7
print('Os valores são: \033[4:31m{}\033[m e \033[4:36m{}\033[m'.format(n1, n2))

nome = input('Qual é o seu nome? ')
print('Seu nome é {}{}{}!!'.format('\033[4:34m', nome, '\033[m'))
#print('\033[35m{}\033[m'.format(nome))