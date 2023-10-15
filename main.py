from pyomo.environ import *
import random
import instances

# #---------------------classes---------------------#

# class node: #vertice tem um id (numero) e uma cor (string)
#     edges = []
#     def __init__(self, id, color):
#         self.id = id
#         self.color = color
#     def __str__(self):
#         return f"[{self.id} {self.color}]"

# class edge: #aresta tem um vertice de origem (u) e um de destino (v
#     def __init__(self, u, cost, v):
#         self.cost = cost

#         self.u = u
#         u.edges.append(self)
#         self.v = v
#         v.edges.append(self)
#     def __str__(self):
#         return f"{self.u} <----> {self.v}"

# class graph: #grafo tem um conjunto de vertices e um conjunto de arestas
#     def __init__(self, nodes, edges):
#         self.nodes = nodes
#         self.edges = edges
#     def __str__(self):
#         return f"{self.nodes} {self.edges}"

# #---------------------methods----------------------#

# colors = instances.colors #cria uma lista de cores aleatorias
# '''
#         ['red',  'blue',   'green',
#         'yellow', 'orange', 'purple',
#         'pink',   'black',  'white',  
#         'brown',  'gray',   'cyan'] '''#cores possiveis

# def create_nodes(n): #cria n vertices com cores aleatorias
#     nodes = []
#     for i in range(n):
#         nodes.append(node(i ,colors[random.randint(0, len(colors)-1)]))
#     return nodes

# def create_edges(n): #cria arestas aleatorias
#     edges = []
#     for i in range(n):
#         edges.append(edge(nodes[random.randint(0, len(nodes)-1)], nodes[random.randint(0, len(nodes)-1)]))
#     return edges   

# def print_graph(graph):
#     print("vertices:")
#     for n in graph.nodes:
#         print(n)
#     print("\ngrafo:")
#     for e in graph.edges:
#         print(e)

# #---------------------main----------------------#
# nodes = create_nodes(instances.total_vertices) #cria vertices do tamanho indicado nas instancias
# edges = create_edges(instances.total_vertices) #cria n arestas
# theGraph = graph(nodes, edges) #cria o grafo

# print("vertices:")
# for n in theGraph.nodes:
#     print(n)

# print("\ngrafo:")
# for e in theGraph.edges:
#     print(e)

# print_graph(theGraph) #printa o grafo

import csv
matrix = []
V = []
E = []
T = []
with open('HomoSapiens_Torque2.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        a = [''] * 3
        for key, j in enumerate(row):
            a[key] = j
            if(a[0] not in V):
                V.append(a[0])
            if(a[2] != '' and a[2] not in E):
                E.append(a[2])
            if(a[1] != ''):
                T.append(a[1])
        matrix.append(a)
        
# # print(matrix)
# print(E)
# print(V.__len__())
# print(E.__len__())
T.sort()
T.reverse()
print(T)
# from pyomo.environ import *

# # Dados do problema
# V = matrix[]  # Lista de vértices
# E = [...]  # Lista de arestas
# num_cores = ...  # Número total de cores
# m = [...]  # Lista de multiplicidades para cada cor

# # Criação do modelo
# model = ConcreteModel()

# # Conjuntos
# model.V = Set(initialize=V)
# model.E = Set(initialize=E)
# model.Cores = RangeSet(num_cores)

# # Variáveis
# model.x = Var(model.V, within=Binary)
# model.y = Var(model.E, within=Binary)

# # Função objetivo
# def objective_function(model):
#     return sum(model.y[u, v] for (u, v) in model.E) - sum(model.x[u] for u in model.V)
# model.obj = Objective(rule=objective_function, sense=minimize)

# # Restrições
# def cor_constraint_rule(model, c):
#     return sum(model.x[u] for u in V_c) == m[c]
# model.cor_constraint = Constraint(model.Cores, rule=cor_constraint_rule)

# def y_constraint_rule(model, u, v):
#     return model.y[u, v] <= model.x[u] * model.x[v]
# model.y_constraint = Constraint(model.E, rule=y_constraint_rule)

# def y_constraint_rule2(model, u, v):
#     return model.y[u, v] <= model.x[v]
# model.y_constraint2 = Constraint(model.E, rule=y_constraint_rule2)

# # Resolvendo o modelo com o solver GLPK
# solver = SolverFactory('glpk')
# results = solver.solve(model)

# # Imprimir resultados
# print("Status da solução:", results.solver.status)
# print("Valor da função objetivo:", model.obj())

# # Imprimir valores das variáveis
# for u in model.V:
#     print(f"x_{u} = {value(model.x[u])}")

# for (u, v) in model.E:
#     print(f"y_{u}_{v} = {value(model.y[u, v])}")

            
# #---------------------pyomo----------------------#

# # model = ConcreteModel()

# # model.x = Var(nodes, domain=Binary)
# # model.y = Var(edges, domain=Binary)
# # model.obj = Objective(expr=sum(model.x[n] for n in nodes) - sum(model.y[uv] for uv in edges), sense=minimize)
