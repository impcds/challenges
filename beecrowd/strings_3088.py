class Texto():
    def __init__(self):
        self.entrada = input()


    def limpa(self):
        self.entrada = self.entrada.replace(' ,', ',')
        self.entrada = self.entrada.replace(' .', '.')

    def __str__(self):
        return self.entrada


try:
    while True:
        obj = Texto()
        obj.limpa()
        print(obj)
except EOFError:
    pass
