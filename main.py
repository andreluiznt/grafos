# -*- coding: utf-8 -*-
from graph import Graph

def load_from(fileName):
    f = open(fileName, 'r')
    n = int(f.readline())
    
    g = Graph(n)
    
    # LEITURA DA MATRIZ DE ADJACÊNCIA
    for l in range(n):
        line = f.readline().strip()
        numeros = line.split("\t")
        for c in range(n):
            g.M[l][c] = int(numeros[c])
            if g.M[l][c] != 0:
                g.L[l].append(c)

    return g

g = load_from("pcv50.txt") # carregar o grafo do arquivo
g.print() # imprimir as representações do grafo
n = g.num_comp() # calculcar e imprimir o número de componentes conexos
print("Número de Componentes: " + str(n)) # realizar e imprimir o caminho entre dois vértices usando BFS

g.print_bfs_path(1, 3)
g.print_bfs_path(2, 5)
