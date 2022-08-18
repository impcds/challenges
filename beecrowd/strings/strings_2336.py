class ABC():
    def __init__(self):
        self.entrada = [ord(i) - 65 for i in input()[::-1]]
        self.m = 1000000007
        self.saida = 0


    def modulo(self, elevado):
        for k, v in enumerate(self.entrada):
            self.saida += v * elevado[k]

    def __str__(self):
        return str(self.saida % self.m)

try:
    l = [26 ** i for i in range(1001)]
    while True:
        obj = ABC()
        obj.modulo(l)
        print(obj)
except EOFError:
    pass
