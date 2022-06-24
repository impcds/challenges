class Tabuada():
    def __init__(self):
        entrada = input().split('x')
        self.fator_um = int(entrada[0])
        self.fator_dois = int(entrada[-1])

    def saida(self):
        if self.fator_um == self.fator_dois:
            for i in range(5, 11):
                print(f'{self.fator_um} x {i} = {self.fator_um * i}')
            return
        for i in range(5, 11):
            print(f'{self.fator_um} x {i} = {self.fator_um * i} && {self.fator_dois} x {i} = {self.fator_dois * i}')


casos = int(input())
for i in range(casos):
    obj = Tabuada()
    obj.saida()
