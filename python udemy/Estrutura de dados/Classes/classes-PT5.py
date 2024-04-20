import datetime
class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nasc):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nasc = ano_nasc
    def complet_info(self):
        return f'{self.nome} {self.sobrenome} {self.ano_nasc}'
    def idade_func(self):
        return f'O Funcionario {self.nome} Tem {datetime.date.today().year - self.ano_nasc} Anos.'


usuario1 = Funcionarios('Doca', 'Augusto', 1995)
print(usuario1.complet_info())
print(Funcionarios.complet_info(usuario1))
print(Funcionarios.idade_func(usuario1))
