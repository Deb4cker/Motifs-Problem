from pyomo.environ import * 
import instances
<<<<<<< HEAD

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
=======
#---------------------main----------------------#
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
#---------------------pyomo----------------------#

# V = instances.V
# E = instances.E
# C = instances.C
# m = instances.m

# model = ConcreteModel()

# model.x = Var(V, domain=Binary)
# model.y = Var(E, domain=Binary)
# model.obj = Objective(expr=sum(model.x[n] for n in V) - sum(model.y[uv] for uv in E), sense=minimize)

# model.con1 = Constraint(expr=sum(model.x[v] for v in V) == sum(m[c] for c in C for v in V if c == instances.I_V_I[v]))
# model.con2 = Constraint(E, rule=lambda model, uv: model.y[uv] <= model.x[uv[0]])
# model.con3 = Constraint(E, rule=lambda model, uv: model.y[uv] <= model.x[uv[1]])
# model.con4 = Constraint(V, rule=lambda model, v: 0 <= model.x[v] <= 1)
# model.con5 = Constraint(E, rule=lambda model, uv: 0 <= model.y[uv] <= 1)

# solver = SolverFactory('glpk')
# results = solver.solve(model)

# print('Status:', results.solver.status)
# print('Termination criterion:', results.solver.termination_condition)
# if results.solver.termination_condition == 'optimal':
#     print('Optimal solution cost:', model.obj.expr())
#     print('Optimal solution is x1 =', model.x[1].value, 'and x2 =', model.x[2].value)
>>>>>>> b9c840b113b78e7bb0af4878e29e1507a2a1b216
