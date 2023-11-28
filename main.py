import instances
import metaheuristic_method
import mathematical_method
import time

# # Dados do problema

nvertex = int(input("Digite o número de vértices: "))
ncolors = int(input("Digite o número de cores: "))

V = instances.generateVertex(nvertex)  # Conjunto de vértices
C = instances.generateColors(ncolors)  # Conjunto de cores
E = instances.generateEdges(V)  # Conjunto de arestas
cores = instances.generateVerticesColors(V, ncolors)
M = instances.generateM(ncolors, cores)
Vc = instances.generateVc(cores, ncolors) # Mapa de cores de cada vértice

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
