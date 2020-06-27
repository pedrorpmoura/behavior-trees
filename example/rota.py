'''

Neste problema pretende-se calcular a rota que um carteiro deve fazer para
entregar encomendas num bairro.

O carteiro quer tentar aliviar peso o mais depressa possível, pelo que tenta
sempre ir primeiro (pelo caminho mais rápido) ao maior prédio do bairro,
continuando depois as entregas pela ordem de tamanhos. 

O mapa do bairro é dado por uma lista de blocos rectangulares 2D, dados pelas
coordenadas do canto inferior esquerdo e superior direito, sendo que quaisquer
dois ou mais blocos que se toquem (ou intersectem) pertencem ao mesmo prédio.
Se existirem dois prédios com o mesmo tamanho, o carteiro visita primeiro o que 
começou a ser definido primeiro no mapa.

O carteiro pode deixar as encomendas de um prédio em qualquer posição que lhe
seja adjacente. Se houver duas posições de um prédio à mesma distância mais
curta, o carteiro dá  prioridade à que estiver mais à esquerda, e, em caso
de empate neste critério, então escolhe a que estiver mais para baixo.

Se um prédio não for acessível então é ignorado, passando o carteiro ao
próximo.

A função a implementar recebe o ponto onde o carteiro começa a visita e o mapa
do bairro. Deve devolver a sequência de pontos onde terá que deixar as encomendas,
intercalada pela respectiva distância.

'''

class Bloco:

    def __init__(self, tuplo):

        self.pontos = set()
        for i in range(tuplo[0], tuplo[2]+1):
            for j in range(tuplo[1], tuplo[3]+1):
                self.pontos.add((i,j))
    

    def __repr__(self):
        return "Bloco({})".format(repr(self.pontos)) 


class Predio:
    
    def __init__(self, bloco_inicial):
        self.pontos = bloco_inicial.pontos
        self.redondezas = set()
        self.atualizar_redondezas()
    
    def adiciona_bloco(self, bloco):
        if len(self.redondezas.intersection(bloco.pontos)) != 0:
            self.pontos = self.pontos.union(bloco.pontos)
            self.atualizar_redondezas()
            return True
        
        return False
    
    def atualizar_redondezas(self):
        self.redondezas = set()
        for (x,y) in self.pontos:
            if (x+1, y) not in self.pontos:
                self.redondezas.add((x+1, y))
            
            if (x-1, y) not in self.pontos:
                self.redondezas.add((x-1, y))
            
            if (x, y+1) not in self.pontos:
                self.redondezas.add((x, y+1))
            
            if (x, y-1) not in self.pontos:
                self.redondezas.add((x, y-1))
    
    def __repr__(self):
        return "Predio({})".format(repr(self.pontos))


def construir_predios(blocos):

    # predio inicial
    predios = { 0: Predio(blocos[0]) }
    c = 1
    for b in blocos[1:]:
        adicionou = 0
        for p in predios:
            if predios[p].adiciona_bloco(b):
                adicionou = 1
        
        if adicionou == 0:
            predios[c] = Predio(b)
            c += 1
    
    return predios


def encontrar_dimensoes_tabuleiro(predios):
    min_x, min_y = (0,0)
    max_x, max_y = (0,0)
    for predio in list(predios.values()):
        for (x,y) in predio.pontos:
            if x < min_x:
                min_x = x
            if y < min_y:
                min_y = y
            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y

    return (min_x-1, min_y-1, max_x+1, max_y+1)


def criar_tabuleiro(predios):

    min_x, min_y, max_x, max_y = encontrar_dimensoes_tabuleiro(predios)
    
    # preencher tabuleiro
    tabuleiro = { (x,y) : None for x in range(min_x, max_x+1) for y in range(min_y, max_y+1)}
    
    for predio in predios:
        pontos = predios[predio].pontos
        for ponto in pontos:
            tabuleiro[ponto] = predio

    return tabuleiro



def obter_adjacentes(posicao_atual, tabuleiro):
    adjacentes = set()
    x, y = posicao_atual

    if (x+1,y) in tabuleiro and tabuleiro[(x+1,y)] == None :
        adjacentes.add((x+1,y))

    if (x-1,y) in tabuleiro and tabuleiro[(x-1,y)] == None:
        adjacentes.add((x-1,y))

    if (x,y+1) in tabuleiro and tabuleiro[(x,y+1)] == None:
        adjacentes.add((x,y+1))

    if (x,y-1) in tabuleiro and tabuleiro[(x,y-1)] == None:
        adjacentes.add((x,y-1))

    return adjacentes


def bfs(posicao_atual, tabuleiro):
    distancias = {}
    queue = []
    distancias[posicao_atual] = 0
    queue.append(posicao_atual)
    while queue:
        c = queue.pop(0)
        for p in obter_adjacentes(c, tabuleiro):
            if p not in distancias:
                distancias[p] = distancias[c] + 1
                queue.append(p)
    
    return distancias


def encontrar_ponto_de_entrega(posicao_atual, predio, distancias):
    pontos = dict()
    for p in predio.redondezas:
        if p not in distancias:
            return False

        pontos[p] = distancias[p]

    
    pontos_ordenados = list(sorted(pontos.items(), key = lambda item: item[1]))
    pontos_minimos = list(filter(lambda par: par[1] == pontos_ordenados[0][1], pontos_ordenados))
    ponto_de_entrega, distancia = sorted(pontos_minimos, key = lambda par: (par[0][0], par[0][1]))[0]
    
    return ponto_de_entrega, distancia



def rota(inicio, blocos):
    rota = [inicio]

    blocos = list(map(Bloco, blocos))
    predios = construir_predios(blocos)
    tabuleiro = criar_tabuleiro(predios)

    
    # rota
    predios_ordenados = sorted(predios.items(), key = lambda item: len(item[1].pontos), reverse = True)
    posicao_atual = inicio

    for i, predio in predios_ordenados:
        distancias = bfs(posicao_atual, tabuleiro)
        
        ponto_de_entrega = encontrar_ponto_de_entrega(posicao_atual, predio, distancias)
        if ponto_de_entrega == False:
            continue
        
        ponto_de_entrega, distancia = ponto_de_entrega
        rota.append(distancia)
        rota.append(ponto_de_entrega)
        posicao_atual = ponto_de_entrega

    return rota

mapa1 = [(0,0,1,1), (3,0,4,0), (3,2,3,3) , (3,3,4,3)]
mapa2 = [(3,0,5,0), (2,2,2,3), (0,3,0,5), (4,3,5,5), (0,5,2,5)]

print(rota((5,0), mapa1))
print(rota((0,0), mapa2))