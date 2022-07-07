import re


class Emoticon():
    def __init__(self, emoticons, linhas):
        self.emoticons = [input() for i in range(emoticons)]
        self.frases = [input() for i in range(linhas)]
        self.nr_alteracoes = 0

    def altera_frase(self, frase):
        emojis = self.emoticons[:]
        alterou = True
        while alterou:
            alterar = False
            emojis, alterar, remover = self.procura_emoji(emojis, frase)
            if alterar:
                frase = frase.replace(remover, ' ', 1)
                self.add_alteracao()
                alterou = True
            else:
                alterou = False

    def procura_emoji(self, emojis, frase):
        menor = len(frase)
        alterar = False
        remover = ''
        for emoji in emojis:
            indice = frase.find(emoji)
            if indice < menor and indice > -1:
                menor = indice
                remover = emoji
                alterar = True
        return emojis, alterar, remover

    def alteracoes(self):
        for frase in self.frases:
            self.altera_frase(frase)

    def add_alteracao(self):
        self.nr_alteracoes += 1

    def __str__(self):
        return str(self.nr_alteracoes)

def le_entrada():
    while True:
        e, f = list(map(int, input().split()))
        if e == 0 and f == 0:
            break
        obj = Emoticon(e, f)
        obj.alteracoes()
        print(obj)
le_entrada()
