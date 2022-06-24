class CartaNatal():
    def __init__(self):
        self.entrada = [letra for letra in input()]

    def __str__(self):
        return ''.join(self.entrada)

    def altera(self):
        for indice, letra in enumerate(self.entrada):
            if letra in ('@&!*#'):
                if letra in '@':
                    self.entrada[indice] = 'a'
                elif letra in '&':
                    self.entrada[indice] = 'e'
                elif letra in '!':
                    self.entrada[indice] = 'i'
                elif letra in '*':
                    self.entrada[indice] = 'o'
                elif letra in '#':
                    self.entrada[indice] = 'u'

try:
    while True:
        obj = CartaNatal()
        obj.altera()
        print(obj)

except EOFError:
    pass
