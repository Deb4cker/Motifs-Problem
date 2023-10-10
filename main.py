from pyomo.environ import *
import random

class node: #vertice tem um id e uma cor
    def __init__(self, id, color):
        self.id: id
        self.color: color
    def __str__(self):
        return f"[{self.id} {self.color}]"

class edge: #aresta tem um vertice de origem e um de destino
    def __init__(self, u, v):
        self.u: u
        self.v: v
    def __str__(self):
        return f"{self.u} -> {self.v}"

colors = ['red',  'blue',   'green',
        'yellow', 'orange', 'purple',
        'pink',   'black',  'white',  
        'brown',  'gray',   'cyan'] #cores possiveis

def create_nodes(n): #cria n vertices com cores aleatorias
    nodes = []
    for i in range(n):
        nodes.append(node(n ,colors[random.randint(0, len(colors)-1)]))
    return nodes

nodes = create_nodes(12)
print(nodes)

#model:

# model = ConcreteModel()
# model.obj = Objective(expr = 1+y, sense=minimize)