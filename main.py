import instances
import metaheuristic_method
import mathematical_method
import time

# # Dados do problema

nvertex = int(input("Digite o número de vértices: "))
ncolors = int(input("Digite o número de cores: "))


# V = [0, 1, 2, 3, 4, 5, 6 ,7, 8, 9] # Conjunto de vértices
# C = [0, 1, 2] # Conjunto de cores
# E =[(4, 5), (9, 3), (0, 6), (7, 5), (3, 8), (8, 6), (1, 2), (5, 6), (2, 6)] # Conjunto de arestas
# Vc = {0: [5], 1: [0, 2, 3, 4, 8, 9], 2: [1, 6, 7]}# Conjunto de vértices e suas cores
# M = [0, 2, 0] #O subgrafo deve ter a quantidade tal para cada cor

V = instances.generateVertex(nvertex)  # Conjunto de vértices
C = instances.generateColors(ncolors)  # Conjunto de cores
E = instances.generateEdges(V)  # Conjunto de arestas
cores = instances.generateVerticesColors(V, ncolors)
M = instances.generateM(ncolors, cores)
Vc = instances.generateVc(cores, ncolors)

print("edges:", E)
print("M", M)
print('Vc', Vc)

start_mathematical = time.time()
mathematical_method.start(V, E, C, Vc, M)
end_mathematical = time.time()
print("Tempo de execução: ", end_mathematical - start_mathematical)
  
start_metaheuristic = time.time()
metaheuristic_method.start(V, E, Vc, M)
end_metaheuristic = time.time()
print("Tempo de execução: ", end_metaheuristic - start_metaheuristic)

# print(colorDictionary)
