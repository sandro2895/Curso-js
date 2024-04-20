class Funcionarios:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

usuario1 = Funcionarios('Doca', 'Augusto', 28)
usuario2 = Funcionarios('Ada', 'Wong', 25)
print(f'{usuario1.nome} {usuario1.sobrenome} {usuario1.idade}')
print(f'{usuario2.nome} {usuario2.sobrenome} {usuario2.idade}')




