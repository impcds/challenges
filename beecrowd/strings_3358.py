class Sobrenome():
    def __init__(self):
        self.sobrenome = input()
        self.consoantes = 0

    def analisa(self):
        vogais = ('AEIOUaeiou')
        for letra in self.sobrenome:
            if letra not in vogais:
                self.consoantes += 1
                if self.consoantes == 3:
                    print(f'{self.sobrenome} nao eh facil')
                    return
            else:
                self.consoantes = 0
        print(f'{self.sobrenome} eh facil')


c = int(input())

for i in range(c):
    obj = Sobrenome()
    obj.analisa()
