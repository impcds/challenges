# time limit exceeded


class PainelLed():
    def __init__(self):
        entrada = input().split()
        self.painel = [i for i in entrada[0]]
        self.nr_leds = len(self.painel)
        self.nr_alternancias = int(entrada[1])

    def alterna_uma(self, x):
        if 'X' in x:
            return 'O'
        return 'X'

    def alterna_todas(self):
        apagou = False
        primeira = self.alterna_uma(self.painel[0])
        self.painel[0] = primeira
        if primeira in 'X':
            apagou = True

        if apagou:
            for led in range(1, self.nr_leds):
                estado = self.alterna_uma(self.painel[led])
                self.painel[led] = estado
                if estado in 'O':
                    apagou = False
                    break

    def alternancias(self):
        for i in range(self.nr_alternancias):
            self.alterna_todas()

    def __str__(self):
        return ''.join(self.painel)

c = int(input())
for i in range(c):
    obj = PainelLed()
    obj.alternancias()
    print(obj)
