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

colorDictionary = generateVerticesWithColors(Vc)
graph = generateGraph(V, E)

# V = generateVertex(nvertex)  # Conjunto de vértices
# C = generateColors(ncolors)  # Conjunto de cores
# E = generateEdges(V)  # Conjunto de arestas
# cores = generateVerticesColors(V, ncolors)
# M = generateM(ncolors, cores)
# Vc = generateVc(cores, ncolors)


