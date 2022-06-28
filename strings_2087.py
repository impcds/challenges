import re

class Conjuntos():
    def __init__(self, nr_frases):
        self.frases = [input() for i in range(nr_frases)]
        self.nr_frases = nr_frases

    def conjunto_ruim(self):
        for indice, frase in enumerate(self.frases):
            for i in range(indice + 1, self.nr_frases):
                print(f'log {indice} - {frase} || {self.frases[i]}')
                if re.match(frase, self.frases[i]):
                    return True

    def bom_ou_ruim(self):
        if self.conjunto_ruim():
            print('Conjunto Ruim')
        else:
            print('Conjunto Bom')

class Conjunto():
    def __init__(self, nr_frases):
        self.frases = []
        self.bom = True
        for i in range(nr_frases):
            nova = input()
            if self.bom:
                self.analisa(nova)
            self.frases.append(nova)

    def analisa(self, frase):
        for i in self.frases:
            if re.match(frase, i):
                self.bom = False
                return


while True:
    c = int(input())
    if c == 0:
        break
    obj = Conjunto(c)
    if obj.bom:
        print('Conjunto Bom')
    else:
        print('Conjunto Ruim')

'''while True:
    c = int(input())
    if c == 0:
        break
    obj = Conjuntos(c)
    obj.bom_ou_ruim()
'''
