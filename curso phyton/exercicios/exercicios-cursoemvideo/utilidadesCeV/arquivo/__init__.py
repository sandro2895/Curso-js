from utilidadesCeV.cadastrosA import *
from utilidadesCeV.cadastrosB import *
def arqexist(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criararq(nome):
    try:
        a = open(nome, 'wt+')
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerarq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler aquivo!')
    else:
        titulo('Pessoas Cadastradas')
        print(a.read())
    finally:
        a.close()


def cadsp(nome):
    try:
        a = open(nome, 'a+')
    except:
        print('Erro ao ler o arquivo! ')
    else:
        while True:
            try:
                b = str(input('Digite o nome de uma pessoa: ')).title ().strip ()
                c = leiaInt('Digite o nome da pessoa: ')
            except:
                print('valor digitado incorreto')
            else:
                break
        a.write(f'{b}               {c}\n')
        a.close()
        print(f'pessoa: {b}  {c} cadastrada com sucessso! ')
