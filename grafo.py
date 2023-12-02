from copy import deepcopy
from utils import nextl, split_st, split_nd

class Vertice:

    def __init__(self, index, label):
        self.__index = index
        self.__label = label

    def __str__(self) -> str:
        return "índice: {}, nome: {}".format(self.__index, self.__label)
       
    def __repr__(self) -> str:
        return "índice: {}, nome: {}".format(self.__index, self.__label)

    @property
    def index(self):
        return self.__index

    @property
    def label(self):
        return self.__label

class Graph:

    def __init__(self, lines : list=[], n : int=0):
        self.__vertices = set()
        self.__edges = dict()
        self.__V = list()
        self.__neighbors = list()

        if lines:
            # inicializa a estrutura que mapeia os vizinhos
            self.__neighbors = [set()] * n
            self.__V = [None] * n

            # leitura dos vértices
            for _ in range(n):
                # lê uma linha
                v, label = split_st(lines[0])
                # adiciona um vértice ao seu conjunto V
                self.__vertices.add(int(v))
                self.__V[int(v) - 1] = Vertice(int(v), label.strip()[1:-1])
                # passa uma linha
                nextl(lines)

            nextl(lines)

            self._add_edges(lines)

    def _add_edges(self, lines):
        # leitura das arestas
        for line in lines:
                
            u, v, w = split_nd(line)
            u, v, w = int(u), int(v), float(w)
            # adiciona a aresta (u, v) ao grafo
            self.__edges[frozenset((u, v))] = w
            # adiciona v aos vizinhos de u
            if not self.__neighbors[u-1]:
                self.__neighbors[u-1] = set((v,))
            else:
                self.__neighbors[u-1].add(v)
            # adiciona u aos vizinhos de v
            if not self.__neighbors[v-1]:
                self.__neighbors[v-1] = set((u,))
            else:
                self.__neighbors[v-1].add(u)

    def neighbors(self, u : int) -> list:
        return list(self.__neighbors[u - 1])
    
    def w(self, e : (int, int)) -> float:
        u, v = e
        
        if v in self.neighbors(u):
            return self.__edges[frozenset((u, v))]
        
        return float('inf')
    
    def vertice(self, v : int) -> Vertice:
        if v in self.__vertices:
            return self.__V[v-1]
        
        return None
       
    @property
    def vertices(self):
         return self.__vertices
    
    @property
    def edges(self):
        return (e for e in self.__edges)
    
    def get_labels(self):
        return (v.label for v in self.__V)
    
    def add_edge(self, e : (int, int), w : int=0):

        if e[0] in self.__vertices and e[1] in self.__vertices:
            # adiciona a aresta ao grafo
            self.__edges[frozenset(e)] = w
            # atualiza os vizinhos do vértice e0
            if not self.__neighbors[e[0]-1]:
                self.__neighbors[e[0]-1] = set((e[1],))
            else:
                self.__neighbors[e[0]-1].add(e[1])
            # atualiza os vizinhos do vértice e1
            if not self.__neighbors[e[1]-1]:
                self.__neighbors[e[1]-1] = set((e[0],))
            else:
                self.__neighbors[e[1]-1].add(e[0])

    def remove_edge(self, e):

        if e[0] in self.__vertices and e[1] in self.neighbors(e[0]):

            # retira a aresta do grafo
            del self.__edges[frozenset(e)]
            # atualiza os vizinhos de ambos os vértices
            self.__neighbors[e[0]-1].remove(e[1])
            self.__neighbors[e[1]-1].remove(e[0])

    def add_vetice(self, v: int, label : str):

        if v not in self.__vertices:
            # adiciona um vértive ao grafo
            self.__vertices.add(v)
            self.__V = self.__V + [None] * (len(self.__neighbors) - (v-1))
            self.__V[v-1] = (Vertice(v, label))
            self.__neighbors = self.__neighbors + [None] * (len(self.__neighbors) - (v-1))
            self.__neighbors[v] = set()


class DiGraph(Graph):
    
    def __init__(self, lines : list=[], n : int=0):
        super().__init__(lines, n)

    def _add_edges(self, lines):
        # leitura dos arcos
        for line in lines:
                
            u, v, w = split_nd(line)
            u, v, w = int(u), int(v), float(w)
            # adiciona o arco (u, v) ao grafo
            self._Graph__edges[(u, v)] = w
            # adiciona v aos vizinhos de u
            if not self._Graph__neighbors[u-1]:
                self._Graph__neighbors[u-1] = set((v,))
            else:
                self._Graph__neighbors[u-1].add(v)
   
    def w(self, e : (int, int)) -> float:
        u, v = e
        
        if v in self.neighbors(u):
            return self._Graph__edges[(u, v)]
        
        return float('inf')
    
    def add_edge(self, e : (int, int), w : int=0):

        if e[0] in self._Graph__vertices and e[1] in self._Graph__vertices:
            # adiciona a aresta ao grafo
            self._Graph__edges[e] = w
            # atualiza os vizinhos do vértice e0
            if not self._Graph__neighbors[e[0]-1]:
                self._Graph__neighbors[e[0]-1] = set((e[1],))
            else:
                self._Graph__neighbors[e[0]-1].add(e[1])

    def remove_edge(self, e):

        if e[0] in self._Graph__vertices and e[1] in self.neighbors(e[0]):

            # retira a aresta do grafo
            del self._Graph__edges[e]
            # atualiza os vizinhos de ambos os vértices
            self._Graph__neighbors[e[0]-1].remove(e[1])
    
    def reversed(self):
        G_ = deepcopy(self)
        # inverte os arcos
        for e in self._Graph__edges:

            w = self.w(e)
            G_.remove_edge(e)
            G_.add_edge((e[1], e[0]), w)

        return G_