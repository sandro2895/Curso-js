from utilidadesCeV import cadastrosB
from utilidadesCeV.arquivo import *
arq = 'exemplo.txt'

if not arqexist(arq):
    criararq(arq)

while True:
    resp = cadastrosB.menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema'])
    if resp == 1:
        # Opção de listar o conteúdo de um arquivo
        lerarq(arq)
    elif resp == 2:
        cadsp(arq)
    elif resp == 3:
        print('Saindo do sistema...'.center(40))
        break
    else:
        print('Digite uma opção valida!')
