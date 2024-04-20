tabela = ('Botafogo', 'Flamengo', 'Palmeiras', 'Grêmio', 'Fluminense',
          'Bragantino', 'Athletico-PR', 'São Paulo', 'Cuiabá', 'Cruzeiro',
          'Fortaleza', 'Internacional', 'Atlético-MG', 'Corinthians', 'Santos',
          'Goiás', 'Bahia', 'Coritiba', 'America-MG', 'Vasco da gama')
print(f'Os cinco primeiros times da tabela são: {tabela[:5]}')
print(f'Os quatro ultimo times da tabela são: {tabela[16:]}')
print(f'Os time em ordem alfabética fica: {sorted(tabela)}')
print(f'O Fortaleza está em {tabela.index("Fortaleza")+1}ª posição')
print(tabela.index("Coritiba")+1)


