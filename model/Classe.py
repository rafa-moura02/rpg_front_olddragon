class Classe:
    def __init__(self):
        self.tipo = None
        self.habilidades = []

    def escolhaClasse(self, escolha):
        if escolha == 1:
            self.tipo = "Guerreiro"
            self.habilidades = [
                "Ataque Poderoso",
                "Defesa com Escudo",
                "Força Bruta"
            ]
        elif escolha == 2:
            self.tipo = "Mago"
            self.habilidades = [
                "Bola de Fogo",
                "Teleporte",
                "Escudo Arcano"
            ]
        elif escolha == 3:
            self.tipo = "Ladrão"
            self.habilidades = [
                "Furtividade",
                "Ataque pelas Costas",
                "Desarme de Armadilhas"
            ]
        else:
            self.tipo = "Desconhecida"
            self.habilidades = []

    def mostrarClasse(self):
        print(f"A classe escolhida foi: {self.tipo}")
        print("Habilidades:")
        for h in self.habilidades:
            print(f"- {h}")
