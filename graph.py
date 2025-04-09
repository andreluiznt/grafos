# -*- coding: utf-8 -*-
import queue

class Graph:
    def __init__(self, n):
        self.num_vertices = n
        self.M = [[0 for _ in range(n)] for _ in range(n)] # Matriz de adjacência
        self.L = [ [] for _ in range(n)] # Lista de adjacência

    # FUNÇÃO PARA IMPRIMIR GRAFO
    def print(self):
        print("Número de Vértices: ", self.num_vertices)
        print("Matriz de adjacência:")
        for row in self.M:
            print(row)
        print("Lista de Adjacência:")
        for adj_list in self.L:
            print(adj_list)
    
    # FUNÇÃO PARA BUSCAR O NÚMERO DE COMPONENTES CONEXOS
    def num_comp(self):
        pred = self.dfs()
        num = 0
        for v in range(self.num_vertices):
            if(pred[v] == -1): # se o vértice não foi visitado
                num += 1
        return num
    
    # BUSCA EM PROFUNDIDADE (DFS) USANDO UMA PILHA
    def dfs(self):
        pred = [-1 for _ in range(self.num_vertices)] # lista de predecessores
        visitados = [False for _ in range(self.num_vertices)] # lista de vértices visitados
        for v in range(self.num_vertices):
            if(visitados[v] == False):
                self.dfs_stack(v, visitados, pred) # chama a DFS iterativa (troquei dfs_rec por dfs_stack)
                
        return pred
        
    # DFS com pilha (eliminando recursão)
    def dfs_stack(self, start, visitados, pred):
        stack = [start]
        visitados[start] = True
        while stack:
            v = stack.pop()
            for u in self.L[v]:
                if not visitados[u]:
                    visitados[u] = True
                    pred[u] = v
                    stack.append(u)
    
    # BUSCA EM LARGURA (BFS)
    def bfs(self, source):
        visitados = [False for _ in range(self.num_vertices)]
        pred = [-1 for _ in range(self.num_vertices)]
        D = [-1 for _ in range(self.num_vertices)] # distâncias
        Q = queue.Queue()
        Q.put(source)
        visitados[source] = True
        D[source] = 0
        
        while(Q.empty() == False):
            v = Q.get()
            print("Vertice:" + str(v))
            for u in self.L[v]:
                if(visitados[u] == False):
                    Q.put(u)
                    visitados[u] = True
                    D[u] = D[v] + 1
                    pred[u] = v
        
        return D, pred
        
    # FUNÇÃO PARA IMPRIMIR O CAMINHO ENTRE DOIS VÉRTICES S E T USANDO BFS
    def print_bfs_path(self, source, target):
        D, pred = self.bfs(source)
        if D[target] == -1:
            print(f"Não há caminho entre os vértices {source} e {target}.")
            return
        
        path = []
        current = target
        while current != -1:
            path.append(current)
            current = pred[current]
        path.append(source)
        path.reverse()
        print(f"Caminho entre {source} e {target}:", " -> ".join(map(str, path)))