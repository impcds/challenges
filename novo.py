import sys

sys.stdin.reconfigure(errors='ignore')
def entrada(self):
    return [i for i in input()]

class Phone():
    def __init__(self):
        self.original = entrada()
        self.comprimento = len(self.original)
        self.timeA = entrada()
        self.timeB = entrada()
        self.acertosA = 0
        self.acertosB = 0
        self.desempateA = 1000
        self.desempateB = 1000
        self.errouA = False
        self.errouB = False



    def analisa(self):
        try:
            for i in range(self.comprimento):
                if self.timeA[i] == self.original[i]:
                    self.acertosA += 1
                else:
                    if not self.errouA:
                        if self.timeB[i] == self.original[i]:
                            self.errouA = True
                            self.desempateA = i

                if self.timeB[i] == self.original[i]:
                    self.acertosB += 1
                else:
                    if not self.errouB:
                        if self.timeA[i] == self.original[i]:
                            self.errouB = True
                            self.desempateB = i
        except:
            pass

    def vitoria(self):
        if self.acertosA > self.acertosB:
            return 'time 1'
        elif self.acertosA < self.acertosB:
            return 'time 2'
        else:
            if self.desempateA > self.desempateB:
                return 'time 1'
            elif self.desempateA < self.desempateB:
                return 'time 2'
            else:
                return 'empate'

c = int(input())

for i in range(1, c + 1):
    a = Phone()
    a.analisa()
    print(f'Instancia {i}')
    print(a.vitoria())
    if i < c:
        print()




class Matring():
    def __init__(self):
        self.matring = [[input()] for i in range(4)]
        self.lenght = len(self.matring[0][0])
        self.m = [[] for i in range(self.lenght)]
        self.transpor()
        self.numerar()
        self.letras()

    def transpor(self):
        for x in range(self.lenght):
            for z in range(4):
                self.m[x].append(self.matring[z][0][x])

    def numerar(self):
        for i in range(self.lenght):
            self.m[i] = int(''.join(self.m[i]))

    def decodificar(self, linha):
        return (((self.m[0] * linha) + self.m[-1]) % 257)

    def letras(self):
        self.voila = ''
        for i in range(1, self.lenght - 1):
            c = self.decodificar(self.m[i])
            self.voila += chr(c)
        print(self.voila)

'''matriz = [[j * i for j in range(1, 8)] for i in range(2, 6)]
matriz = [[input()] for i in range(4)]
nova = [[] for i in range(7)]
print(matriz)

for i in matriz:
    print(i)

for i in nova:
    print(i)
'''
class Matringa():
    def __init__(self):
        self.matring = []
        self.f = ''
        self.l = ''

        for i in range(4):
            self.matring.append(input())

        self.m = [[] for i in range(len(self.matring))]

        for i in range(4):
            self.f += self.matring[i][0]
            self.l += self.matring[i][-1]

        for i in range(len(self.matring)):
            aux = ''
            lista = []
            for j in range(4):
                self.m[j][j].append(self.matring[j][i])

        self.f = int(self.f)
        self.l = int(self.l)





class Kaaa():
    def __init__(self):
        self.entrada = input()
        self.k = self.entrada.find('k')
        self.antes = self.entrada.count('a', 0, self.k)
        self.depois = self.entrada.count('a', self.k)
        self.total = self.antes * self.depois


    def saida(self):
        print(f'k{"a" * self.total}')

    def __str__(self):
        return self.entrada + 'k' + ('a' * self.total)

# c = int(input())
# for i in range(c):
#     a = Kaaa()
#     a.saida()

class Parenteses():
    def __init__(self):
        self.entrada = input()
        self.parenteses = ''
        for i in self.entrada:
            if i in '()':
                self.parenteses += i

    def valida(self):
        while self.parenteses:
            lenAntes = len(self.parenteses)
            self.parenteses = self.parenteses.replace('()', '')
            lenDepois = len(self.parenteses)
            if lenAntes == lenDepois:
                print('incorrect')
                break
        if not self.parenteses:
            print('correct')
'''
try:
    while True:
        a = Parenteses()
        a.valida()
except EOFError:
    pass
'''

'''class Contador():
    def __init__(self):
        self.maior = 0
        self.saida = []
        while True:
            entrada = input()
            if entrada == '0':
                self.imprimeSaida()
                break
            else:
                self.frase = entrada.split()
                self.contagem()

    def contagem(self):
        self.caracteres = []
        for i in self.frase:
            tamanho = len(i)
            self.caracteres.append(tamanho)
            if tamanho >= self.maior:
                self.maior = tamanho
                self.palavra = i
        self.saida.append(self.caracteres)


    def imprimeSaida(self):
        for i in self.saida:
            a = '-'.join(map(str, i))
            print(a)
        print()
        print(f'The biggest word: {self.palavra}')

a = Contador()
'''
'''class Inteiro():
    def __init__(self):
        self.entrada = input().strip().replace(' ', '').replace('.', '').replace(',', '')
        self.entrada = self.entrada.replace('l', '1').replace('O', '0').replace('o', '0')


    def valido(self):
        try:
            self.inteiro = int(self.entrada)
            if self.inteiro <= 2147483647:
                print(self.inteiro)
            else:
                print('error')
        except Exception as e:
            print('error')

try:
    while True:
        obj = Inteiro()
        obj.valido()
except EOFError:
    pass
'''
'''
class Palavras():
    def __init__(self):
        self.letras = 0
        self.palavras = 0
        self.media = 0
        self.dificuldade = 250
        self.entrada = input().split()

    def __str__(self):
        return str(self.dificuldade)

    def contagem(self):
        for i in self.entrada:
            if i.isalpha():
                self.palavras += 1
                self.letras += len(i)
            else:
                if i.endswith('.') and i.count('.') == 1:
                    t = i.replace('.', '')
                    if t.isalpha():
                        self.letras += len(t)
                        self.palavras += 1

    def medirMedia(self):
        try:
            self.media = self.letras // self.palavras
        except ZeroDivisionError:
            pass

    def nivel(self):
        if self.media <= 3:
            self.dificuldade = 250
        elif self.media >= 6:
            self.dificuldade = 1000
        else:
            self.dificuldade = 500

try:
    while True:
        a = Palavras()
        a.contagem()
        a.medirMedia()
        a.nivel()
        print(a)
except EOFError:
    pass
'''
'''class Numero():
    def __init__(self):
        self.num = str(float(input())).split('.')
        self.inteiro = int(self.num[0])
        self.fracao = float(f'0.{self.num[1]}')
        self.cutoff = float(input())

    def saida(self):
        if self.fracao > self.cutoff:
            print(self.inteiro + 1)
        else:
            print(self.inteiro)


try:
    while True:
        a = Numero()
        a.saida()
except EOFError:
    pass
'''



'''
class Desenho():
    def __init__(self, altura, largura):
        self.original = []
        self.novo = [[] for i in range(altura)]
        self.altura = altura
        self.largura = largura

        for i in range(altura):
            self.original.append(input())

        self.novaMedidas = list(map(int, input().split()))
        self.novaAltura = int(self.novaMedidas[0] / self.altura)
        self.novaLargura = int(self.novaMedidas[1] / self.largura)

        for i in range(self.altura):
              for j in self.original[i]:
                  self.novo[i] += j * self.novaLargura
              self.novo[i] = ''.join(self.novo[i])

        for i in range(self.altura):
            for j in range(self.novaAltura):
                print(self.novo[i])

while True:
    a, b = list(map(int, input().split()))
    if a == b == 0:
        break
    else:
        c = Desenho(a, b)
'''
'''try:
    while True:
        palavra = [i for i in input()]
        saida = ' '.join(palavra)
        tamanho = len(saida)
        aux = tamanho
        while tamanho > 0:
            print(f'{saida:>{aux}}')
            palavra.pop()
            saida = ' '.join(palavra)
            tamanho = len(saida)
            aux -= 1
        print()
except EOFError:
    pass
'''
'''
c = int(input())

class Dieta():
    def __init__(self):
        self.dieta = input()
        self.cafe = input()
        self.almoco = input()
        self.comeu = self.cafe + self.almoco
        self.cheater = False
        self.janta = ''
        self.analisa()
        self.jantar()
        self.enfim()

    def analisa(self):
        for i in self.comeu:
            if i not in self.dieta:
                self.cheater = True
                break

        if len(set(self.comeu)) != len(self.comeu):
            self.cheater = True


    def jantar(self):
        for i in self.dieta:
            if i not in self.comeu:
                self.janta += i
        l = [i for i in self.janta]
        l.sort()
        self.janta = ''.join(l)

    def enfim(self):
        if not self.cheater:
            print(self.janta)
        else:
            print('CHEATER')

for i in range(c):
    a = Dieta()


class Ciclos():
    def __init__(self):
        self.rastro = input()
        self.processo = int(input())
        self.leituras = 0
        self.ciclos = 0
        self.calculaCiclos()


    def calculaCiclos(self):
        for i in self.rastro:
            if i in 'W':
                if self.leituras:
                    self.ciclos += 2
                    self.leituras = 0
                else:
                    self.ciclos += 1
            else:
                self.leituras += 1
                if self.leituras == self.processo:
                    self.ciclos += 1
                    self.leituras = 0
        if self.leituras:
            self.leituras = 0
            self.ciclos += 1

        print(self.ciclos)
'''

'''try:
    while True:
        a = Ciclos()
except EOFError:
    pass'''


'''

def tesoura(oponente):
    if oponente in ['papel', 'lagarto']:
        return 'v'
    elif oponente in ['spock', 'pedra']:
        return 'd'
    else:
        return 'e'

def papel(oponente):
    if oponente in ['pedra', 'spock']:
        return 'v'
    elif oponente in ['tesoura', 'lagarto']:
        return 'd'
    else:
        return 'e'

def pedra(oponente):
    if oponente in ['lagarto', 'tesoura']:
        return 'v'
    elif oponente in ['papel', 'spock']:
        return 'd'
    else:
        return 'e'

def spock(oponente):
    if oponente in ['tesoura', 'pedra']:
        return 'v'
    elif oponente in ['lagarto', 'papel']:
        return 'd'
    else:
        return 'e'

def lagarto(oponente):
    if oponente in ['spock', 'papel']:
        return 'v'
    elif oponente in ['pedra', 'tesoura']:
        return 'd'
    else:
        return 'e'


def s():
    print('sheldon')

def r():
    print('rajesh')

def e():
    print('empate')

c = int(input())

for i in range(c):
    rajesh, sheldon = input().split()
    if sheldon in ['tesoura']:
        if rajesh in ['papel', 'lagarto']:
            s()
        elif rajesh in ['spock', 'pedra']:
            r()
        else:
            e()
    elif sheldon in 'papel':
        if rajesh in ['pedra', 'spock']:
            s()
        elif rajesh in ['tesoura', 'lagarto']:
            r()
        else:
            e()
    elif sheldon in 'pedra':
        if rajesh in ['lagarto', 'tesoura']:
            s()
        elif rajesh in ['papel', 'spock']:
            r()
        else:
            e()
    elif sheldon in 'spock':
        if rajesh in ['tesoura', 'pedra']:
            s()
        elif rajesh in ['lagarto', 'papel']:
            r()
        else:
            e()
    elif sheldon in 'lagarto':
        if rajesh in ['spock', 'papel']:
            s()
        elif rajesh in ['pedra', 'tesoura']:
            r()
        else:
            e()


'''
'''
try:
    while True:
        primeira = input()
        segunda = input()
        tam = len(primeira)


        for i in primeira[]


        res = [primeira[x:y] for x, y in combinations(range(len(primeira) + 1), r = 2)]
        maior = 0
        res.sort(key=len, reverse=True)
        print(res)
        for i in res:
            if i in segunda:
                maior = len(i)
                break
        print(maior)

except EOFError:
    pass

'''


'''c = int(input())

posicao = {
            'esquerda': False,
            'centro': True,
            'direita': False
}

def leObstaculos():
    return input().strip().replace(' ', '')

def calculaToques(posicao, obstaculos):
    toques = 0
    if posicao['esquerda']:
        if '110' in obstaculos:
            toques += 2
            posicao['esquerda'] = False
            posicao['direita'] = True
        elif '101' in obstaculos:
            toques += 1
            posicao['esquerda'] = False
            posicao['centro'] = True
    elif posicao['centro']:
        if '110' in obstaculos:
            toques += 1
            posicao['centro'] = False
            posicao['direita'] = True
        elif '011' in obstaculos:
            toques += 1
            posicao['centro'] = False
            posicao['esquerda'] = True
    elif posicao['direita']:
        if '011' in obstaculos:
            toques += 2
            posicao['direita'] = False
            posicao['esquerda'] = True
        elif '101' in obstaculos:
            toques += 1
            posicao['direita'] = False
            posicao['centro'] = True

    return toques

toques = 0
for i in range(c):
    obstaculos = leObstaculos()
    toques += calculaToques(posicao, obstaculos)
fim = input()
print(toques)
'''
