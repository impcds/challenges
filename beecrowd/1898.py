#import sys
#sys.stdin.reconfigure(encoding='ISO-8859-1')
# Usado para deixar explicito o codec necessário para decodificar a entrada.


class Propina():
    def __init__(self):
        self.primeira = input()
        self.segunda = input()
        self.cpf = ''

    def elimina_nao_numericos(self, string):
        saida = ''
        for character in string:
            if character.isnumeric() or character in '.':
                saida += character

        return saida

    def encontra_cpf(self):
        for index, character in enumerate(self.primeira):
            if character.isnumeric():
                self.cpf += character
                if len(self.cpf) == 11:
                    self.primeira = self.primeira[index + 1:]
                    break

    def encontra_propina(self, string):
        ponto = string.find('.')
        if ponto > -1:
            string = string[:ponto + 3]
            return string
        return string

obj = Propina()
obj.primeira = obj.elimina_nao_numericos(obj.primeira)
obj.segunda = obj.elimina_nao_numericos(obj.segunda)
obj.encontra_cpf()
print(f'cpf {obj.cpf}')
propina_um = float(obj.encontra_propina(obj.primeira))
propina_dois = float(obj.encontra_propina(obj.segunda))
print(f'{propina_um + propina_dois:.2f}')
