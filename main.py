from pyomo.environ import *
import random

#---------------------classes---------------------#

class node: #vertice tem um id (numero) e uma cor (string)
    def __init__(self, id, color):
        self.id = id
        self.color = color
    def __str__(self):
        return f"[{self.id} {self.color}]"

class edge: #aresta tem um vertice de origem (u) e um de destino (v
    def __init__(self, u, v):
        self.u = u
        self.v = v
    def __str__(self):
        return f"{self.u} <----> {self.v}"

class graph: #grafo tem um conjunto de vertices e um conjunto de arestas
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
    def __str__(self):
        return f"{self.nodes} {self.edges}"

#---------------------methods----------------------#

colors = ['red',  'blue',   'green',
        'yellow', 'orange', 'purple',
        'pink',   'black',  'white',  
        'brown',  'gray',   'cyan'] #cores possiveis

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

#---------------------main----------------------#

nodes = create_nodes(12) #cria 12 vertices
edges = create_edges(12) #cria 12 arestas
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
    
#model:

# model = ConcreteModel()
# model.obj = Objective(expr = 1+y, sense=minimize)