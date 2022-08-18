class Abrevia():
    def __init__(self, inpu):
        self.palavras = {chr(i): [] for i in range(97, 123)}
        self.palavras_a_trocar = {chr(i): [] for i in range(97, 123)}
        self.avaliacoes = {chr(i): [] for i in range(97, 123)}
        self.entrada = inpu
        self.lista_de_palavras = inpu.split()
        self.lista_de_saida = []
        self.aconchega()

    def aconchega(self):
        for i in self.lista_de_palavras:
            self.palavras[i[0]].append(i)

        for k, v in self.palavras.items():
            self.palavras_a_trocar[k] = set(v)

    def avalia_melhor_troca(self):
        for k, v in self.palavras_a_trocar.items():
            for palavra in v:
                if len(palavra) > 2:
                    a = self.lista_de_palavras.count(palavra)
                    b = len(palavra)
                    total_antes_abreviar = a * b
                    total_depois_abreviar = a * 2
                    total_diminuido = total_antes_abreviar - total_depois_abreviar
                    self.avaliacoes[k].append((total_diminuido, palavra))
            self.avaliacoes[k].sort(reverse=True)

    def efetiva_trocas(self):
        for k, v in self.avaliacoes.items():
            if v:
                for indice, palavra in enumerate(self.lista_de_palavras):
                    if v[0][1] == palavra:
                        self.lista_de_palavras[indice] = k + '.'
                        self.lista_de_saida.append(k + '.' + ' = ' + palavra)

        self.lista_de_saida = set(self.lista_de_saida)
        self.lista_de_saida = list(self.lista_de_saida)
        self.lista_de_saida.sort()

    def saida(self):
        print(' '.join(self.lista_de_palavras))
        print(len(self.lista_de_saida))
        for i in self.lista_de_saida:
            print(i)

while True:
    inp = input()
    if inp == '.':
        break
    obj = Abrevia(inp)
    obj.avalia_melhor_troca()
    obj.efetiva_trocas()
    obj.saida()
