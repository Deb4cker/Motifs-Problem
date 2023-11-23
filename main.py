from pyomo.environ import *
from instances import *

#codigo solução	

def deep_walk(level, visited, queue, graph, current_delta):
    for s in queue:
        if s not in S:
            for neighbor in graph.item(s):
                if neighbor in S:
                    nNeighborsInS = count(graph.item(s))
                    current_delta[s] - 1 - nNeighborsInS
                elif current_delta[neighbor] < current_delta[s]:
                    current_delta[s] - current_delta[neighbor] + 1
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
            queue.remove(0)
            visited.add(s)
            
def solve(S, graph, Visited):
    for s in S:
        level = 0
        current_delta = []
        for v in graph.get(s):
            deep_walk(level, Visited, graph, current_delta)

# # Dados do problema

nvertex = int(input("Digite o número de vértices: "))
ncolors = int(input("Digite o número de cores: "))

# V = generateVertex(nvertex)  # Conjunto de vértices
# C = generateColors(ncolors)  # Conjunto de cores
# E = generateEdges(V)  # Conjunto de arestas
# cores = generateVerticesColors(V, ncolors)
# M = generateM(ncolors, cores)
# Vc = generateVc(cores, ncolors)

V = [0, 1, 2, 3, 4, 5, 6 ,7, 8, 9] # Conjunto de vértices
C = [0, 1, 2] # Conjunto de cores
E = [(6, 9), (5, 7), (6, 0), (6, 8), (6, 1), (3, 4), (4, 9)] # Conjunto de arestas
Vc = {0: [2, 4, 0, 9, 6], 1: [3, 5], 2: [1, 8, 7]} # Conjunto de vértices e suas cores
M = [2, 1, 1] #O subgrafo deve ter a quantidade tal para cada cor]
G = generateGraph(V, E) #Grafo G
Visited = [] #Conjunto de vértices visitados
S = [] #Conjunto solução

colorDictionary = generateVerticesWithColors(Vc, V)
grades = generateGrades(G, V)

solve(S, G, Visited)

#1 #Atualiza os deltas
#2 #Acha o melhor delta
#3 #repete o passo 1 até que seja satisfeito o M
#4 imprime o conjunto solução
