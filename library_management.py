# Content Library Management: Managing a library of streaming content, including movies and TV shows

class Midia:
    def __init__(self, tipo, titulo, genero, classificacao, tempo_duracao):
        self.tipo = tipo
        self.titulo = titulo
        self.genero = genero
        self.classificacao = classificacao
        self.tempo_duracao = tempo_duracao
# aplicar subclasses para o exibir informações ser diferente e mais facil de entender; aqui vamos estudar o conceito
# entenderemos o conceito de herança aq
    def exibir_informacoes(self):
        print("╔" + "═" * 50 + "╗")
        print(f"║ 🎬  {self.titulo:<42}║")
        print("╠" + "═" * 50 + "╣")
        print(f"║ Tipo: {self.tipo:<42}║")
        print(f"║ Gênero: {self.genero:<40}║")
        print(f"║ Classificação: {self.classificacao:<32}║")
        
        if self.tipo.lower() == "série" and hasattr(self, 'episodios') and hasattr(self, 'temporadas'):
            print(f"║ Episódios: {self.episodios:<40}║")
            print(f"║ Temporadas: {self.temporadas:<38}║")
        else:
            print(f"║ Duração: {self.tempo_duracao} min{'':<31}║")

        print("╚" + "═" * 50 + "╝")




def todas_as_midias():
    midias = []

    # Ação
    midias.append(Midia("Filme", "Mad Max: Estrada da Fúria", "Ação", "16+", 120))
    midias.append(Midia("Série", "The Walking Dead", "Ação", "16+", 45))
    midias.append(Midia("Filme", "John Wick", "Ação", "16+", 101))
    midias.append(Midia("Série", "Game of Thrones", "Ação", "18+", 60))
    midias.append(Midia("Filme", "Vingadores: Ultimato", "Ação", "12+", 181))
