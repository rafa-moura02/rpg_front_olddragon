class Atributos:
    def __init__(self):
        from .JogarDado import JogarDado
        self.j = JogarDado()
        self.AtributosRandom = {
            "forca": None,
            "destreza": None,
            "constituicao": None,
            "inteligencia": None,
            "sabedoria": None,
            "carisma": None
        }

    def gerar_clássico(self):
        for nome in self.AtributosRandom.keys():
            self.AtributosRandom[nome] = self.j.jogarTresDadosESomar()

    def gerar_valores_aventureiro(self):
        return [self.j.jogarTresDadosESomar() for _ in range(6)]

    def gerar_valores_heroico(self):
        valores = []
        for _ in range(6):
            resultado = self.j.valorDado()
            resultado.remove(min(resultado))
            valores.append(sum(resultado))
        return valores

    def distribuir_valores(self, escolhas, valores):
        """
        escolhas: lista de atributos escolhidos pelo usuário
        valores: lista de valores gerados
        """
        for atributo, valor in zip(escolhas, valores):
            if atributo in self.AtributosRandom:
                self.AtributosRandom[atributo] = valor

    def descricao(self, atributo, valor):
        if valor is None:
            return "Não definido"

        descricoes = {
            "forca": {(3, 8): "Fraco", (9, 12): "Mediano", (13, 16): "Forte", (17, 18): "Muito Forte"},
            "destreza": {(3, 8): "Letárgico", (9, 12): "Mediano", (13, 16): "Ágil", (17, 18): "Preciso"},
            "constituicao": {(3, 8): "Frágil", (9, 12): "Mediano", (13, 16): "Resistente", (17, 18): "Vigoroso"},
            "inteligencia": {(3, 8): "Inepto", (9, 12): "Mediano", (13, 16): "Inteligente", (17, 18): "Gênio"},
            "sabedoria": {(3, 8): "Tolo", (9, 12): "Mediano", (13, 16): "Intuitivo", (17, 18): "Presciente"},
            "carisma": {(3, 8): "Descortês", (9, 12): "Mediano", (13, 16): "Carismático", (17, 18): "Magnético"}
        }

        for (inicio, fim), desc in descricoes.get(atributo, {}).items():
            if inicio <= valor <= fim:
                return desc
        return "Indefinido"

    def atributos_com_descricoes(self):
        resultado = {}
        for nome, valor in self.AtributosRandom.items():
            if valor is None:
                resultado[nome] = {"valor": "-", "descricao": "Não definido"}
            else:
                resultado[nome] = {"valor": valor, "descricao": self.descricao(nome, valor)}
        return resultado
