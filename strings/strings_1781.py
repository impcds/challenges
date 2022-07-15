class Guga():
    def __init__(self):
        self.vogais = []
        self.consoantes = []
        self.frase = [self.vogais.append((i, z)) if z in 'aeiou' else self.consoantes.append((i, z)) for i, z in enumerate(input())]
        self.operacoes = [list(map(int, input().split())) for i in range(int(input()))]
        self.deslocar_vogal = 0
        self.deslocar_consoante = 0
        self.vogal = True
        self.consoante = True

    def __str__(self):
        return ''.join(self.frase)

    def permuta(self, sequencia, posicoes):
        '''Recebe uma lista contendo as tuplas a serem alteradas e o numero de posicoes
        a deslocar cada item.'''
        letras = []
        indices = []
        tamanho = len(sequencia)
        if tamanho == 0 or tamanho == 1 or posicoes % tamanho == 0:
            return sequencia
        if posicoes > tamanho:
            posicoes = posicoes % tamanho
        for i in sequencia:
            letras.append(i[1])
            indices.append(i[0])
        letras = letras[tamanho - posicoes:] + letras[:tamanho - posicoes]
        return list(zip(indices, letras))

    def agregar(self):
        '''Verifica a necessidade de alterar as vogais ou consoantes na frase original
        e realiza as trocas'''
        if self.vogal:
            self.vogal = False
            for i in self.vogais:
                self.frase[i[0]] = i[1]
        if self.consoante:
            self.consoante = False
            for i in self.consoantes:
                self.frase[i[0]] = i[1]

    def opera(self):
        '''Verifica cada operacao pedida, adicionando o numero de posicoes a deslocar
        para vogal ou consoante, e chamando a funcao que realiza as trocas.'''
        for i in self.operacoes:
            if i[0] == 0:
                self.deslocar_vogal += i[1]
                self.vogal = True
                continue
            if i[0] == 1:
                self.deslocar_consoante += i[1]
                self.consoante = True
                continue
            if i[0] == 2:
                self.deslocar()
                print(self)

    def deslocar(self):
        if self.vogal:
            self.vogais = self.permuta(self.vogais, self.deslocar_vogal)
        if self.consoante:
            self.consoantes = self.permuta(self.consoantes, self.deslocar_consoante)
        self.agregar()

for i in range(int(input())):
    obj = Guga()
    print(f'Caso #{i + 1}:')
    obj.opera()
