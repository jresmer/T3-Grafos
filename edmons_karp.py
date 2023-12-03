from grafo import DiGraph
from math import inf

def edmonds_karp(G: DiGraph, s: int, t: int):
    
    f = 0

    while 1:

        ca = bfs(G, s, t)

        if not ca:

            break

        edges = []

        for i in range(len(ca) - 1):

            edges.append((ca[i], ca[i+1]))

        fp = min([G.w(e) for e in edges])
        f += fp

        for u, v in edges:

            current_w = G.w((u, v))
            G.remove_edge((u, v))
            G.add_edge((u, v), current_w - fp)
            current_w = G.w((v, u))
            G.remove_edge((v, u))
            G.add_edge((v, u), current_w + fp)

    return f

def bfs(G: DiGraph, s: int, t: int):

    c = [False for v in G.vertices]
    a = [None for v in G.vertices]
    c[s-1] = True

    q = list()

    q.append(s)

    while q:

        u = q.pop(0)

        for v in G.neighbors(u):

            if not c[v-1] and G.w((u, v)) > 0:

                q.append(v)

                c[v-1] = True
                a[v-1] = u

                if v == t:

                    p = [t]
                    w = t

                    while w != s:

                        w = a[w-1]
                        p.insert(0, w)

                    return p
    
    return []

def prepare_residual_network(G: DiGraph):

    edges = [e for e in G.edges]

    for u, v in edges:

        if (v, u) in G.edges:

            weight = G.w((u, v))

            G.remove_edge((u, v))

            new_v = len(G.vertices)
            G.add_vetice(new_v, new_v)
            G.add_edge((u, new_v), weight)
            G.add_edge((new_v, u), 0)
            G.add_edge((new_v, v), weight)
            G.add_edge((v, new_v), 0)
        else:

            G.add_edge((v, u), 0)

    return G

def find_s_t(G: DiGraph):
    
    s = None
    t = None

    for v in G.vertices:

        label = G.vertice(v).label

        if label == "s":
            s = v
        elif label == "t":
            t = v

    return s, t
