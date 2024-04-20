class Funcionarios:
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome} {self.idade}'



usuario1 = Funcionarios('doca', 'Augusto', 28)
usuario2 = Funcionarios('Sandro', 'Augusto', 58)

print(usuario1.nome_completo())
print(usuario2.nome_completo())
print(Funcionarios.nome_completo(usuario1))
print(Funcionarios.nome_completo(usuario2))

