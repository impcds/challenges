class Telefone():
    def __init__(self):
        self.entrada = input()
        self.saida = ''
        self.teclas = {
                '1': '1',
                '2': '2ABCabc',
                '3': '3DEFdef',
                '4': '4GHIghi',
                '5': '5JKLjkl',
                '6': '6MNOmno',
                '7': '7PQRSpqrs',
                '8': '8TUVtuv',
                '9': '9WXYZwxyz',
                '0': '0'
                }

    def __str__(self):
        return self.saida

    def analisa_entrada(self):
        for i in self.entrada:
            if i.isalnum():
                for k, v in self.teclas.items():
                    if i in v:
                        self.saida += k
                        break
            elif i in '#*':
                self.saida += i

try:
    while True:
        obj = Telefone()
        obj.analisa_entrada()
        print(obj)
except:
    pass
