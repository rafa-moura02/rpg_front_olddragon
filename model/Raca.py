class Raca:
    def __init__(self):
        self.raca = None
        self.movimento = None
        self.infravisao = None
        self.alinhamento = None
        self.peso = None
        self.idades = None
        self.habilidades = []

    def escolhaRaca(self, raca):
        if raca == 1:
            self.raca = "Elfo"
            self.habilidades = ["Visão no Escuro", "Precisão com Arcos", "Afinidade com Magia"]
        elif raca == 2:
            self.raca = "Anão"
            self.habilidades = ["Resistência a Veneno", "Força Subterrânea", "Afinidade com Mineração"]
        elif raca == 3:
            self.raca = "Humano"
            self.habilidades = ["Adaptabilidade", "Versatilidade", "Determinação"]
        elif raca == 4:
            self.raca = "Gnomo"
            self.habilidades = ["Truques Ilusionistas", "Resistência Mental", "Astúcia"]
        elif raca == 5:
            self.raca = "Meio Elfo"
            self.habilidades = ["Carisma Natural", "Versatilidade Cultural", "Equilíbrio de Raças"]
        elif raca == 6:
            self.raca = "Halfling"
            self.habilidades = ["Sorte Incomum", "Furtividade", "Agilidade Natural"]
        else:
            self.raca = "Desconhecida"
            self.habilidades = []

    def atributosRaca(self, idade):
        if self.raca == "Elfo":
            self.movimento = "9 metros"
            self.infravisao = "18 metros"
            self.alinhamento = "Neutro"
            self.peso = 60
            if idade < 120:
                self.idades = "Jovem"
            elif idade < 450:
                self.idades = "Adulto"
            elif idade < 900:
                self.idades = "Meia-Idade"
            else:
                self.idades = "Idoso"

        elif self.raca == "Anão":
            self.movimento = "6 metros"
            self.infravisao = "18 metros"
            self.alinhamento = "Ordem"
            self.peso = 75
            if idade < 50:
                self.idades = "Jovem"
            elif idade < 120:
                self.idades = "Adulto"
            elif idade < 350:
                self.idades = "Meia-Idade"
            else:
                self.idades = "Idoso"

        elif self.raca == "Humano":
            self.movimento = "9 metros"
            self.infravisao = "Não"
            self.alinhamento = "Qualquer"
            self.peso = 80
            if idade < 15:
                self.idades = "Jovem"
            elif idade < 45:
                self.idades = "Adulto"
            elif idade < 90:
                self.idades = "Meia-Idade"
            else:
                self.idades = "Idoso"

        elif self.raca == "Gnomo":
            self.movimento = "6 metros"
            self.infravisao = "18 metros"
            self.alinhamento = "Neutro"
            self.peso = 40
            if idade < 20:
                self.idades = "Jovem"
            elif idade < 150:
                self.idades = "Adulto"
            elif idade < 350:
                self.idades = "Meia-Idade"
            else:
                self.idades = "Idoso"

        elif self.raca == "Meio Elfo":
            self.movimento = "9 metros"
            self.infravisao = "9 metros"
            self.alinhamento = "Caos"
            self.peso = 65
            if idade < 25:
                self.idades = "Jovem"
            elif idade < 80:
                self.idades = "Adulto"
            elif idade < 180:
                self.idades = "Meia-Idade"
            else:
                self.idades = "Idoso"

        elif self.raca == "Halfling":
            self.movimento = "6 metros"
            self.infravisao = "Não"
            self.alinhamento = "Neutro"
            self.peso = 35
            if idade < 20:
                self.idades = "Jovem"
            elif idade < 50:
                self.idades = "Adulto"
            elif idade < 100:
                self.idades = "Meia-Idade"
            else:
                self.idades = "Idoso"

        else:
            self.raca = "Desconhecida"

    def mostrarAtributos(self):
        print(f"Raça: {self.raca}")
        print("Habilidades:")
        for h in self.habilidades:
            print(f"- {h}")
        print(f"Movimento: {self.movimento}")
        print(f"Infravisão: {self.infravisao}")
        print(f"Alinhamento: {self.alinhamento}")
        print(f"Peso base: {self.peso} kg")
        print(f"Classificação por idade: {self.idades}")
