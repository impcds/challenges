class Gaga():
    def __init__(self):
        self.entrada = input()
        self.tamanho_entrada = len(self.entrada)
        self.meio = int(len(self.entrada) / 2)

    def separa(self):
        self.inicio = self.entrada[:self.meio]
        self.final = self.entrada[self.meio:]

    def aumenta_metade(self):
        self.meio += 1

    def analisa_final(self):
        return self.inicio.endswith(self.final)

    def remove_gaguejada(self):
        self.separa()
        if not self.analisa_final():
            if self.meio == self.tamanho_entrada:
                return
            self.aumenta_metade()
            self.remove_gaguejada()

    def __str__(self):
        return self.inicio

try:
    while True:
        obj = Gaga()
        obj.remove_gaguejada()
        print(obj)
except EOFError:
    pass
