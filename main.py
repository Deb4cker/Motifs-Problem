import instances
import solver

# # Dados do problema

nvertex = int(input("Digite o número de vértices: "))
ncolors = int(input("Digite o número de cores: "))


# V = [0, 1, 2, 3, 4, 5, 6 ,7, 8, 9] # Conjunto de vértices
# C = [0, 1, 2] # Conjunto de cores
# E = [(6, 2), (5, 7), (8, 2), (9, 0), (4, 2), (7, 1), (0, 1), (3, 2), (2, 1)] # Conjunto de arestas
# Vc = {0: [0, 2, 5, 7], 1: [3, 4, 8, 9], 2: [1, 6]} # Conjunto de vértices e suas cores
# M = [0, 3, 1] #O subgrafo deve ter a quantidade tal para cada cor

V = instances.generateVertex(nvertex)  # Conjunto de vértices
C = instances.generateColors(ncolors)  # Conjunto de cores
E = instances.generateEdges(V)  # Conjunto de arestas
cores = instances.generateVerticesColors(V, ncolors)
M = instances.generateM(ncolors, cores)
Vc = instances.generateVc(cores, ncolors)

print("edges:", E)
print("M", M)
print('Vc', Vc)

# motifs = find_motifs(V, E, Vc, M

#choose aleatory vertex
#iterate in each connected vertex until have tha pattern [2 of color 0, 1 of color 1 and 1 of color 2]
#while this, mount the motif
#insert the motif in a solution array
#search for the next vertex
#repeat the process until not have more vertex to search
#get the motif with the min count in the array of solutions
#print this motif as the solution

graph = instances.generateGraph(V, E)

degrees = instances.generateDegrees(graph, V)

print(solver.start(degrees, graph, V, Vc, M))

# print(colorDictionary)
