nome = input('Qual é o seu nome? ')
cores = {'limpa': '\033[30m',
         'azul': '\033[34m',
         'vermelho': '\033[31m'}
print('Seu nome é {}{}{}'.format(cores['vermelho'], nome, cores['limpa']))
