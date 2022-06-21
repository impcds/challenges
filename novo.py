class Cabo():
    def __init__(self, casos):
        self.casos = casos
        self.nomes = [input() for i in range(casos)]
        self.valores = [sum([ord(x) for x in i]) for i in self.nomes]
        self.cont = 0

    def times(self, x=0):
        self.timeA = self.nomes[:x]
        self.timeB = self.nomes[x:]
        self.valoresA = self.valores[:x]
        self.valoresA.reverse()
        self.valoresB = self.valores[x:]
        self.valoresA = sum((self.potencia(self.valoresA)))
        self.valoresB = sum((self.potencia(self.valoresB)))

    def potencia(self, lista):
        if lista:
            return [valor * (i + 1)  for i, valor in enumerate(lista)]
        return []

    def compara_igualdade(self):
        self.times(self.cont)
        if self.valoresA == self.valoresB:
            print(f'{self.timeA[-1]}')
            return
        self.cont += 1
        if self.cont > self.casos:
            print("Impossibilidade de empate.")
            return
        self.compara_igualdade()


while True:
    c = int(input())
    if c == 0:
        break

    obj = Cabo(c)
    obj.compara_igualdade()





class Jetiqui():
    def __init__(self):
        self.first = input()
        self.second = input()
        self.enigma = input()


    def vai(self):
        first_letter = self.enigma.find('_')
        second_letter = self.enigma.find('_', first_letter + 1)
        first = self.first[first_letter]
        first += self.first[second_letter]
        second = self.second[first_letter]
        second += self.second[second_letter]

        if first[0] == second[1] or first[1] == second[0]:
            return True
        else:
            return False

    def __str__(self):
        if self.vai():
            return 'Y'
        else:
            return 'N'

class Zoeiro():
    def __init__(self, x, z):
        self.trocas = [input() for i in range(x)]
        self.sentencas = [input() for i in range(z)]

    def decodifica(self):
        for i in self.sentencas:
            saida = ''
            for l in i:
                trocou = False
                for t in self.trocas:
                    if l in t[0]:
                        saida += t[2]
                        trocou = True
                    elif l in t[2]:
                        saida += t[0]
                        trocou = True
                if not trocou:
                    saida += l
            print(saida)


class Hopper():
    def __init__(self):
        self.entrada = input().lower().split('-')
        self.letras = [self.letras(i) for i in self.entrada]
        self.meta = 'cobol'

    def letras(self, palavra):
        return (palavra[0], palavra[-1])

    def cobol(self):
        for k, v in enumerate(self.meta):
            if v not in self.letras[k]:
                return False
        return True

    def __str__(self):
        if self.cobol():
            return 'GRACE HOPPER'
        else:
            return 'BUG'

class Jon():
    def __init__(self):
        self.string = input()
        self.r = self.string[:self.string.find('+')]
        self.l = self.string[self.string.find('+') + 1:self.string.find('=')]
        self.j = self.string[self.string.find('=') + 1:]

    def __str__(self):
        return self.string

    def encontraX(self):
        if self.r.isnumeric() and self.l.isnumeric():
            return int(self.r) + int(self.l)
        elif self.r.isnumeric() and self.j.isnumeric():
            return int(self.j) - int(self.r)
        elif self.l.isnumeric() and self.j.isnumeric():
            return int(self.j) - int(self.l)

class Evergreen():
    def __init__(self):
        self.first = input()
        self.second = input()
        self.first_name = ''
        self.last_name = ''

    def __str__(self):
        return self.first_name

    def conversor(self):
        for i in range(0, len(self.first), 2):
            self.first_name += self.first[i:i+2]
            self.first_name += self.second[i:i+2]


class Turing():
    def __init__(self):
        self.cifrada = input()
        self.crib = input()
        self.len_cifrada = len(self.cifrada)
        self.len_crib = len(self.crib)
        self.possibilidades = 0

    def __str__(self):
        return str(self.possibilidades)

    def analisa(self):
        inicio = 0
        while inicio - 1 < self.len_cifrada - self.len_crib:
            inicio += self.compara(inicio)

    def compara(self, inicio):
        aux = self.cifrada[inicio:inicio + self.len_crib]
        for i in range(self.len_crib):
            if self.crib[i] == aux[i]:
                return 1
        self.possibilidades += 1
        return 1

class TempPassword():
    def __init__(self):
        self.entrada = input()
        self.password = ''

    def __str__(self):
        return self.password

    def validador(self):
        try:
            if len(self.entrada) != 20 or self.entrada[:2] != 'RA':
                self.password = 'INVALID DATA'
            else:
                self.password = self.entrada[2:].lstrip('0')
        except:
            self.password = 'INVALID DATA'

'''c = int(input())
for i in range(c):
    obj = TempPassword()
    obj.validador()
    print(obj)
'''

class Gago():
    def __init__(self):
        self.frase = input().split()

    def __str__(self):
        return ' '.join(self.frase)

    def arrumaGago(self):
        for k, v in enumerate(self.frase):
            try:
                if v[0] == v[2] and v[1] == v[3]:
                    self.frase[k] = self.frase[k][2:]
            except:
                pass

'''try:
    while True:
        obj = Gago()
        obj.arrumaGago()
        print(obj)
except EOFError:
    pass
'''

class AlienAlphabet():
    def __init__(self):
        self.vogais = input()
        self.txt = input()
        self.count = 0

    def __str__(self):
        return str(self.count)

    def contarVogais(self):
        for i in self.vogais:
            self.count += self.txt.count(i)

'''try:
    while True:
        obj = AlienAlphabet()
        obj.contarVogais()
        print(obj)
except:
    pass
'''
class Tags():
    def __init__(self):
        self.old = input()
        self.new = input()
        self.doc = input()
        self.lenTag = len(self.old)
        self.docLower = self.doc.lower()
        self.abreFecha = []
        self.tags = []
        self.tagsValidas = []
        self.valido = True

    def listarIndices(self):
        self.lista_de_indices = []
        for i in range(0, len(self.indices), 2):
            self.lista_de_indices.extend([i for i in range(self.indices[i] + 1, self.indices[i + 1])])

    def alterar(self):
        if self.valido:
            i = 0
            while True:
                i = self.doc.lower().find(self.old.lower(), i + 1)
                self.encontraTags()
                self.listarIndices()
                if i != -1 and i in self.lista_de_indices:
                    self.doc = self.doc[:i] + self.new + self.doc[i + self.lenTag:]
                elif i == -1:
                    break

    def encontraTags(self):
        self.indices = []
        for k, v in enumerate(self.doc):
            if v in '<':
                self.abreFecha.append(v)
                self.indices.append(k)
            elif v in '>':
                self.abreFecha.append(v)
                self.indices.append(k)

    def validacao(self):
        for i in range(0, len(self.abreFecha), 2):
            if self.abreFecha[i] not in '<' or self.abreFecha[i + 1] not in '>':
                self.valido = False
                break

'''try:
    while True:
        obj = Tags()
        obj.encontraTags()
        obj.validacao()
        obj.listarIndices()
        obj.alterar()
        print(obj.doc)
except EOFError:
    pass
'''

class Faixa():
    def __init__(self):
        self.entrada = [j for j in input().replace(' ', '')]

    def eliminarRepetidos(self):
        self.unico = set(self.entrada)
        self.unico = [x for x in self.unico]
        self.unico.sort()

    def faixa(self):
        size = len(self.unico)
        aux = []
        aux.append(self.unico[0])
        for i in range(1, size):
            if ord(self.unico[i]) - ord(self.unico[i - 1]) == 1:
                if i == size - 1:
                    aux.append(self.unico[i])
                else:
                    pass
            else:
                aux.append(self.unico[i-1])
                aux.append(self.unico[i])
                if i == size - 1:
                    aux.append(self.unico[i])

        self.unico = aux[:]

    def saida(self):
        if self.unico:
            size = len(self.unico)
            if size == 1:
                print(f'{self.unico[0]}:{self.unico[0]}')
            for i in range(1, size, 2):
                if i < size - 1:
                    print(f'{self.unico[i - 1]}:{self.unico[i]}', end=', ')
                else:
                    print(f'{self.unico[i - 1]}:{self.unico[i]}')
        else:
            print()

'''try:
    while True:
        a = Faixa()
        a.eliminarRepetidos()
        if a.unico:
            a.faixa()
        a.saida()
except EOFError:
    pass
'''

#import sys
# Usado para deixar explicito o codec necessário para decodificar a entrada.
#sys.stdin.reconfigure(encoding='ISO-8859-1')

def entrada():
    return [j for j in sys.stdin.readline()]

class Phone():
    def __init__(self):
        self.original = entrada()
        self.comprimento = len(self.original)
        self.timeA = entrada()
        self.timeB = entrada()
        self.acertosA = []
        self.acertosB = []

    def analisa(self):
        for k, v in enumerate(self.original):
            try:
                if self.timeA[k] == v:
                    self.acertosA.append(True)
                else:
                    self.acertosA.append(False)
            except:
                self.acertosA.append(True)
            try:
                if self.timeB[k] == v:
                    self.acertosB.append(True)
                else:
                    self.acertosB.append(False)
            except:
                self.acertosB.append(True)

    def desempate(self):
        for i in range(self.comprimento):
            if self.acertosA[i] and not self.acertosB[i]:
                return 'time 1'
            elif not self.acertosA[i] and self.acertosB[i]:
                return 'time 2'
        return 'empate'

    def vitoria(self):
        timea = sum(self.acertosA)
        timeb = sum(self.acertosB)
        if timea > timeb:
            return 'time 1'
        elif timea < timeb:
            return 'time 2'
        else:
            return self.desempate()

'''c = sys.stdin.readline()
c = int(c)

for x in range(1, c + 1):
    a = Phone()
    a.analisa()
    print(f'Instancia {x}')
    vai = a.vitoria()
    print(vai)
    print()
'''

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
