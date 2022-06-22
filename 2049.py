class Ahmoc():
    def __init__(self, c):
        self.assinatura = c
        self.painel = input()

    def quente(self):
        if self.assinatura in self.painel:
            return True
        return False

casos = []
while True:
    c = input()
    if c == '0':
        break

    obj = Ahmoc(c)
    casos.append(obj.quente())

nr_casos = len(casos)
final = '\n'

for instancia, item in enumerate(casos):
    print(f'Instancia {instancia + 1}')
    if item == True:
        print('verdadeira', end='')#, end=final)
    else:
        print('falsa', end='')#, end=final)

    if instancia + 1 < nr_casos:
        print()
        print()
