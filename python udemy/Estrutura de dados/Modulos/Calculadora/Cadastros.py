def clientes():
    print('Cadastro de clients')


def find_index(to_find, item):
    for pos, valor in enumerate(to_find):
        if valor == item:
            return f'Item localizado no index {pos}.'
    return 'Item não localizado!'
