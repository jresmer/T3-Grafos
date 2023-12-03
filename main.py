import sys
from os import path
from coloracao import lawer
from edmons_karp import prepare_residual_network, edmonds_karp, find_s_t
from grafo import Graph, DiGraph
from utils import nextl

def read(file_path: str) -> Graph or DiGraph:

    with open(file_path) as f:

        lines = list(iter(f))

        # lê o número de vértices contidos no grafo
        n = int((lines[0].split())[-1])
        # passa a primeira linha da lista
        nextl(lines)
        
        if lines[n].strip() == " ":
            if lines[n+1].strip() == "*edges":
                return Graph(lines, n)
            else:
                return DiGraph(lines, n)
        
        if lines[n].strip() == "*edges":
            return Graph(lines, n)
        else:
            return DiGraph(lines, n)
    
def main():
    if __name__ == "__main__":

        # execução padrão
        if len(sys.argv) == 1:
            
            # 1) Fluxo Máximo
            print("1) Edmonds-Karp")
            directory = path.join("Instances", "fluxo_maximo", "fluxo_maximo_aula.net")
            G = read(directory)
            G = prepare_residual_network(G)
            s, t = find_s_t(G)
            print("Fluxo Máximo: ", end="")
            print(edmonds_karp(G, s, t))
            print()

            # 3) Coloração Mínima
            print("3) Coloração")
            directory = path.join("Instances", "coloracao", "cor3.net")
            G = read(directory)
            print("Coloração mínima: ", end="")
            print(lawer(G))
            print()

        # execução: "Usage: python3 main.py [Directory] [algorithm]"
        elif len(sys.argv) == 3:
        
            directory = sys.argv[1]
            algorith = sys.argv[2]

            G = read(directory)

            match algorith:

                # 1) Fluxo Máximo
                case "1":
                    G = prepare_residual_network(G)
                    s, t = find_s_t(G)
                    print("Fluxo Máximo: ", end="")
                    print(edmonds_karp(G, s, t))
                    print()
                # 2) Emparelhamento Máximo
                case "2":
                    print("Emparelhamento Máximo Não Implementado")
                # 3) Coloração Mínima
                case "3":
                    print("Coloração mínima: ", end="")
                    print(lawer(G))
                    print()
        # erro
        else:
            sys.exit("Usage: python3 main.py or python3 main.py [Directory] [algorithm]")

main()