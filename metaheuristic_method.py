import instances
import solver

def start(V, E, Vc, M):
  graph = instances.generateGraph(V, E)
  degrees = instances.generateDegrees(graph, V)

  vertexes, number_of_connections = solver.start(degrees, graph, V, Vc, M)
  
  print()
  print("================== Solução Mataheurística ==================")
  print("Solução ótima:", number_of_connections, "Motfis")
  print("Vértices selecionados:")
  print(sorted(vertexes))
  