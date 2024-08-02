class Musica:
    def __init__(self, nome='', artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

    def __str__(self):
        return f"Música: {self.nome.ljust(14)} | Artista(s): {self.artista.ljust(19)} | Duração: {self.duracao} segundos"    
musica1 = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao=248)
musica2 = Musica(nome='Há Tempos', artista='Legião Urbana', duracao=190)
musica3 = Musica(nome='O Girassol', artista='Ira!', duracao=215)

print("Coleção de Músicas:\n")
print(musica1)
print(musica2)
print(musica3)
