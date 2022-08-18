import re

class Conjunto():
    def __init__(self, nr_frases):
        self.frases = {chr(i): [] for i in range(97, 123)}
        self.bom = True
        for i in range(nr_frases):
            nova = input()
            self.frases[nova[0]].append(nova)
        self.analisa()

    def analisa(self):
        for k, v in self.frases.items():
            if v:
                v.sort()
                tamanho = len(v)
                for indice, value in enumerate(v):
                    for j in range(indice + 1, tamanho):
                        if re.match(v[indice], v[j]):
                            self.bom = False
                            return
    def __str__(self):
        if self.bom:
            return 'Conjunto Bom'
        return 'Conjunto Ruim'


while True:
    c = int(input())
    if c == 0:
        break
    obj = Conjunto(c)
    print(obj)
