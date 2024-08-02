class Livro:
    def __init__(self, titulo='', autor='', paginas=0):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f'{self.titulo} por {self.autor} - {self.paginas} páginas'

    @property
    def titulo_autor(self):
        return f'{self.titulo} por {self.autor}'

    def aumentar_paginas(self, quantidade):
        self.paginas += quantidade

livro1 = Livro('1984','Gerorge Orwell', 416)
livro1.aumentar_paginas(20)
print(livro1)

class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = int(idade)
        self.profissao = profissao

    def __str__(self):
        return f'Nome: {self.nome} | Idade: {self.idade} | Profissão: {self.profissao} |'

    def aniversario(self, niver):
        self.idade += niver

    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}.'
        else:
            return f'Olá, sou {self.nome}!'


pessoa1 = Pessoa('José', 23, 'Cozinheiro')
print(pessoa1)
pessoa1.aniversario(1)
print("Função aniversário aplicada")
print(pessoa1)
print(pessoa1.saudacao)