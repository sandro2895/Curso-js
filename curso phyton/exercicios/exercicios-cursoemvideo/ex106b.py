c = ('\033[m',  # 0 <- Sem cor
     '\033[0;30;41m',  # 1 <- Vermelho
     '\033[42m',  # 2 <- Verde
     '\033[7m',  # 3 <- Branco
     '\033[44m',  # 4 <- Azul
     )

def ajuda(com):
    print(c[4], end='')
    print(f'Acessando o manuel do {com}')
    print(c[0], end='')
    print(c[3], end='')
    help(com)
    print(c[0], end='')


def titulo(msg, cor=0):
    tam = len(msg)
    print(c[cor], end=' ')
    print(f'~~{"~" * tam}~~')
    print(f'  {msg}')
    print(f'~~{"~" * tam}~~')
    print(c[0], end='')



# Programa Principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHelp', 2)
    comando = str(input('Função ou Bliblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)
