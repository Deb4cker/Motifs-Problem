from pyomo.environ import *
import random

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
        return f"{self.u} -> {self.v}"

class graph: #grafo tem um conjunto de vertices e um conjunto de arestas
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
    def __str__(self):
        return f"{self.nodes} {self.edges}"


colors = ['red',  'blue',   'green',
        'yellow', 'orange', 'purple',
        'pink',   'black',  'white',  
        'brown',  'gray',   'cyan'] #cores possiveis

def create_nodes(n): #cria n vertices com cores aleatorias
    nodes = []
    for i in range(n):
        nodes.append(node(i ,colors[random.randint(0, len(colors)-1)]))
    return nodes

nodes = create_nodes(12) #cria 12 vertices

def create_edges(n): #cria arestas aleatorias
    edges = []
    for i in range(n):
        edges.append(edge(nodes[random.randint(0, len(nodes)-1)], nodes[random.randint(0, len(nodes)-1)]))
    return edges   

edges = create_edges(12) #cria 12 arestas

for n in nodes:
    print(n)

print("\ngrafo:")

for e in edges:
    print(e)
#model:

# model = ConcreteModel()
# model.obj = Objective(expr = 1+y, sense=minimize)