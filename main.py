from pyomo.environ import *
import random
import instances

#---------------------classes---------------------#

class node: #vertice tem um id (numero) e uma cor (string)
    edges = []
    def __init__(self, id, color):
        self.id = id
        self.color = color
    def __str__(self):
        return f"[{self.id} {self.color}]"

class edge: #aresta tem um vertice de origem (u) e um de destino (v
    def __init__(self, u, cost, v):
        self.cost = cost

        self.u = u
        u.edges.append(self)
        self.v = v
        v.edges.append(self)
    def __str__(self):
        return f"{self.u} <----> {self.v}"

class graph: #grafo tem um conjunto de vertices e um conjunto de arestas
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
    def __str__(self):
        return f"{self.nodes} {self.edges}"

#---------------------methods----------------------#

colors = instances.colors #cria uma lista de cores aleatorias
'''
        ['red',  'blue',   'green',
        'yellow', 'orange', 'purple',
        'pink',   'black',  'white',  
        'brown',  'gray',   'cyan'] '''#cores possiveis

def create_nodes(n): #cria n vertices com cores aleatorias
    nodes = []
    for i in range(n):
        nodes.append(node(i ,colors[random.randint(0, len(colors)-1)]))
    return nodes

def create_edges(n): #cria arestas aleatorias
    edges = []
    for i in range(n):
        edges.append(edge(nodes[random.randint(0, len(nodes)-1)], nodes[random.randint(0, len(nodes)-1)]))
    return edges   

def print_graph(graph):
    print("vertices:")
    for n in graph.nodes:
        print(n)
    print("\ngrafo:")
    for e in graph.edges:
        print(e)

#---------------------main----------------------#
nodes = create_nodes(instances.total_vertices) #cria vertices do tamanho indicado nas instancias
edges = create_edges(instances.total_vertices) #cria n arestas
theGraph = graph(nodes, edges) #cria o grafo

print("vertices:")
for n in theGraph.nodes:
    print(n)

print("\ngrafo:")
for e in theGraph.edges:
    print(e)

print_graph(theGraph) #printa o grafo

import csv
matrix = []
with open('dm.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        a = ['a'] * 3
        for key, j in enumerate(row):
            a[key] = j
            
        matrix.append(a)
        
print(matrix)
            
#---------------------pyomo----------------------#

# model = ConcreteModel()

# model.x = Var(nodes, domain=Binary)
# model.y = Var(edges, domain=Binary)
# model.obj = Objective(expr=sum(model.x[n] for n in nodes) - sum(model.y[uv] for uv in edges), sense=minimize)
