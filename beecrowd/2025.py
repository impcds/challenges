class Santa():
    def __init__(self):
        self.entrada = input().split()

    def analisa(self):
        saida = []
        for word in self.entrada:
            if 'oulupukk' in word:
                if len(word) == 10:
                    saida.append('Joulupukki')
                else:
                    saida.append('Joulupukki.')
            else:
                saida.append(word)

        return ' '.join(saida)

for i in range(int(input())):
    obj = Santa()
    p = obj.analisa()
    print(p)
