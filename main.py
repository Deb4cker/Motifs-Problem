from pyomo.environ import *
import instances
from instances import *

# # Dados do problema

nvertex = int(input("Digite o número de vértices: "))
ncolors = int(input("Digite o número de cores: "))

V = [0, 1, 2, 3, 4, 5, 6 ,7, 8, 9] # Conjunto de vértices
C = [0, 1, 2] # Conjunto de cores
E = [(6, 9), (5, 7), (6, 0), (6, 8), (6, 1), (3, 4), (4, 9)] # Conjunto de arestas
Vc = {0: [2, 4, 0, 9, 6], 1: [3, 5], 2: [1, 8, 7]} # Conjunto de vértices e suas cores
M = [2, 1, 1] #O subgrafo deve ter a quantidade tal para cada cor

# V = generateVertex(nvertex)  # Conjunto de vértices
# C = generateColors(ncolors)  # Conjunto de cores
# E = generateEdges(V)  # Conjunto de arestas
# cores = generateVerticesColors(V, ncolors)
# M = generateM(ncolors, cores)
# Vc = generateVc(cores, ncolors)
solucoes = [2, 1, 5, 6, 3]
solution = generateSolution(V) # Solução inicial
edgeCountList = countEdges(V, E) # Lista de contagem de arestas
randomvertice = 6 # Vértice aleatório  
connectedvertices = getConnectedVertices(V, E, randomvertice)
colorsOfConnectedVertices = getColorsOfVertices(connectedvertices, Vc)
print(M)
print(E)
print(Vc)
print(solution)
print(edgeCountList)
print(randomvertice)
print(connectedvertices)
print(colorsOfConnectedVertices)

vertex_colors = getColorsOfVertices(V, Vc)
motifs = find_motifs(V, E, Vc, M)

#choose aleatory vertex
#iterate in each connected vertex until have tha pattern [2 of color 0, 1 of color 1 and 1 of color 2]
#while this, mount the motif
#insert the motif in a solution array
#search for the next vertex
#repeat the process until not have more vertex to search
#get the motif with the min count in the array of solutions
#print this motif as the solution