import sys
from os import path
from grafo import Graph, DiGraph
from utils import nextl

def read(file_path: str) -> Graph or DiGraph:

    with open(file_path) as f:

        lines = list(iter(f))

        # lê o número de vértices contidos no grafo
        n = int((list(lines)[0].split())[-1])
        # passa a primeira linha da lista
        nextl(lines)

        return Graph(lines, n) if lines[n].strip() == "*egdes" else DiGraph(lines, n)
    
def main():
    if __name__ == "__main__":

        # execução padrão
        if len(sys.argv) == 1:
            
            # 1) Componentes fortemente conexas
            print("1) Componentes fortemente conexas")
            directory = path.join("instances", "arvore_geradora_minima", "agm_tiny.net")
            G = read(directory)
            
            print()

            # 2) Ordenação topologica
            print("2) Ordenação topologica")
            directory = path.join("instances", "extras", "ot_tiny.net")
            G = read(directory)
            
            print()

            # 3) Árvore geradora mínima (Kruskal)
            print("2) Ordenação topologica")
            directory = path.join("instances", "arvore_geradora_minima", "agm_tiny.net")
            G = read(directory)
            
            print()

        # execução: "Usage: python3 main.py [Directory] [algorithm]"
        elif len(sys.argv) == 3:
        
            directory = sys.argv[1]
            algorith = sys.argv[2]

            G = read(directory)

            match algorith:

                # 1) Componentes fortemente conexas
                case "1":
                    ...
                # 2) Ordenação topologica
                case "2":
                    ...
                # 3) Árvore geradora mínima (Kruskal)
                case "3":
                    ...
                # Todos
                case _:
                    ...
        # erro
        else:
            sys.exit("Usage: python3 main.py or python3 main.py [Directory] [algorithm]")

main()