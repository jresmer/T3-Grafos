from grafo import Graph
from math import inf
from utils import powerset, f

def im(G: Graph):
    s = list(powerset(G.vertices))
    s = sorted(s, key=lambda a: len(a), reverse=True)
    r = set()

    for x in s:

        c = True
        for v in x:

            for u in x:

                if frozenset(u, v) in G.edges:
                    
                    c = False
                    break

        if c == True:

            for ss in s:

                if set(ss) - set(x) != set(ss):
                    s.remove(ss)
                
            r = r | x

    return r

def lawer(G: Graph):

    x = [None for i in range(len(G.vertices))]
    x[0] = 0
    # gera a lista de subconjuntos de V
    s = list(powerset(G.vertices))
    # garante a ordenação de acordo com f
    s.sort()    # ordena de acordo com os elementos 1 antes de 2, 3, 4...
    s.sort(key=lambda a: len(a))    # ordena de acordo com o tamanho do subconjunto [] antes de [1] antes de [1,2]...

    for ss in s:

        sn = f(ss)
        x[sn] = inf
        # constrói grafo G'
        G_ = Graph()
        # adiciona os vértices do subconjunto
        for v in ss:

            G_.add_vetice(v, str(v))
        # adiciona as arestas de G em que ambos os vértices pertencem ao subconjunto ss
        for u, v in G.edges:
            
            if u in G_.vertices and v in G_.vertices:
                G_.add_edge((u, v), 1)
        
        for i in im(G_):

            ii = f(list(set(ss) - set(i)))
            if x[ii] + 1 < x[sn]:
                x[sn] = x[i] + 1

    return x[-1]
