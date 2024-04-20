def linha(l):
    lin = '~' * len (l)
    print(f'~~{lin}~~')
    print(f'  {l}')
    print(f'~~{lin}~~')
    print('\033[m')

def ajuda():
    def linha(l):
        lin = '~' * len(l)
        print(f'~~{lin}~~')
        print(f'  {l}')
        print(f'~~{lin}~~')
        print('\033[m')
    print('\033[42m')
    linha('SISTEMA DE AJUDA PyHelp')
    ajuda = str(input('Função ou Bliblioteca  > ')).strip()
    while ajuda != 'fim':
        print('\033[7m')
        help(ajuda)
        print('\033[m')
        print('\033[42m')
        linha('SISTEMA DE AJUDA PyHelp')
        ajuda = str(input('Função ou Bliblioteca  > ')).strip()
        print('\033[7m')
        help(ajuda)
        print('\033[m')
    print('\033[41m')
    linha('ATE LOGO')
    print('\033[m')


ajuda()
