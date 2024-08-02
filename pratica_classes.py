class Carro():
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = int(ano)

carro1 = Carro('Honda Fit', 'Cinza', 2015)



class Restaurante():
    def __init__(self, nome, categoria, avaliacao, ano_fundacao, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.avaliacao = int(avaliacao)
        self.ano_fundacao = int(ano_fundacao)
        self.ativo = ativo
    
    def __str__(self):
        return f'Nome: {self.nome} | Categoria: {self.categoria} | Ano fundação: {self.ano_fundacao} | Avaliação: {self.avaliacao}'

restaurante1 = Restaurante('Habibs', 'Esfiha', 4, 1988)

print(restaurante1)



class Cliente():
    def __init__(self, nome, idade, altura, cpf):
        self.nome = nome
        self.idade = int(idade)
        self.altura = int(altura)
        self.cpf = int(cpf)

    def __str__(self):
        return f'''
Nome: {self.nome}
Idade: {self.idade}
Altura: {self.altura}
CPF: {self.cpf}
                '''
    
cliente1 = Cliente('Joaquim', 73, 190, 12345678983)

print(cliente1)