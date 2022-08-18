class Abreviacao():
    def __init__(self):
        self.frase = input().split()
        self.iniciais = {palavra[0]: [] for palavra in self.frase}

    def agrupa(self):
        for palavra in self.frase:
            self.iniciais[palavra[0]].append(palavra)

    
