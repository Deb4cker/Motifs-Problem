from pyomo.environ import *
import csv
import numpy as np  

# #---------------------classes---------------------#

class vertice:
    vertices = {}

    def __init__(self, color):
        self.name = color
        self.edges = []

        if color not in vertice.vertices:
            vertice.vertices[color] = self

    def __str__(self):
        return f"[{self.name}]"

class edge: #aresta tem um vertice de origem (u) e um de destino (v
    def __init__(self, u, cost, v):
        self.cost = cost

        self.u = u
        u.edges.append(self)
        self.v = v
        v.edges.append(self)
    def __str__(self):
        return f"{self.u} >--{self.cost}--< {self.v}"

#---------------------main----------------------#

V = []
E = []
with open('sc.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)

    first_column = []
    third_column = []
    for row in reader:
        u, cost, v = row
        if u not in vertice.vertices:
            V.append(vertice(u))
            vertice(u)

        if v not in vertice.vertices:
            V.append(vertice(v))
            vertice(v)

        E.append(edge(vertice.vertices[u], cost, vertice.vertices[v]))
        first_column.append(row[0])
        third_column.append(row[2])

    V = set(first_column + third_column)
    V = np.array(list(V))

print(f"{V.__len__()} \n ------------------------------ \n");
for v in V:
    print(v)

print(f"{E.__len__()} \n ------------------------------ \n");
for e in E:
    print(e)

#---------------------pyomo----------------------#

# model = ConcreteModel()

# model.x = Var(nodes, domain=Binary)
# model.y = Var(edges, domain=Binary)
# model.obj = Objective(expr=sum(model.x[n] for n in nodes) - sum(model.y[uv] for uv in edges), sense=minimize)
