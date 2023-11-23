from pyomo.environ import * 
import instances
# #---------------------main----------------------#
selection = input("Choose instances: \nDrosophila melanogaster [1] \nHomo sapiens [2] \nSaccharomyces cerevisiae [3] \n")

if selection == '1':
 table = "dm.csv"
elif selection == '2':
 table = "hs.csv"
elif selection == '3':
 table = "sc.csv"
else:
 print("Invalid selection.")
 exit()

instances.generateGraph(table)

for v in instances.V:
    print(v)

for e in instances.E:
    print(e)    

print(f"\nTotal de vertices: {instances.I_V_I}")
print(f"Total de arestas: {len(instances.E)}") 
print(f"Total de cores: {len(instances.I_C_I)}") #Ellipsis
print(f"Total de vertices com cores repetidas: {instances.I_VM_I}") #Ellipsis
print(f"Tamanho do motif: {instances.I_M_I}") #Ellipsis
print(f"Quantas cores tem no motif: {instances.I_CM_I}") #Ellipsis
# #---------------------pyomo----------------------#


# # Dados do problema

# nvertex = int(input("Digite o número de vértices: "))
# ncolors = int(input("Digite o número de cores: "))


V = [0, 1, 2, 3, 4, 5, 6 ,7, 8, 9] # Conjunto de vértices
C = [0, 1, 2] # Conjunto de cores
E = [(6, 9), (5, 7), (6, 0), (6, 8), (6, 1), (3, 4), (4, 2), (6,5), (1,4)] # Conjunto de arestas
Vc = {0: [2, 4, 0, 9, 6], 1: [3, 5], 2: [1, 8, 7]} # Conjunto de vértices e suas cores
M = [2, 1, 1] #O subgrafo deve ter a quantidade tal para cada cor



# V = generateVertex(nvertex)  # Conjunto de vértices
# C = generateColors(ncolors)  # Conjunto de cores
# E = generateEdges(V)  # Conjunto de arestas
# cores = generateVerticesColors(V, ncolors)
# M = generateM(ncolors, cores)
# Vc = generateVc(cores, ncolors)

# motifs = find_motifs(V, E, Vc, M

#choose aleatory vertex
#iterate in each connected vertex until have tha pattern [2 of color 0, 1 of color 1 and 1 of color 2]
#while this, mount the motif
#insert the motif in a solution array
#search for the next vertex
#repeat the process until not have more vertex to search
#get the motif with the min count in the array of solutions
#print this motif as the solution

colorDictionary = generateVerticesWithColors(Vc, V)
graph = generateGraph(V, E)

print(depth_search(graph.get(6), graph, [6], V))
    
# print(colorDictionary)
