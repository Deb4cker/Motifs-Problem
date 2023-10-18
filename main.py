from pyomo.environ import *
import instances
from instances import *

# # Dados do problema

nvertex = int(input("Digite o número de vértices: "))
ncolors = int(input("Digite o número de cores: "))

V = generateVertex(nvertex)  # Conjunto de vértices
C = generateColors(ncolors)  # Conjunto de cores
E = generateEdges(V)  # Conjunto de arestas
cores = generateVerticesColors(V, ncolors)
M = generateM(ncolors, cores)
Vc = generateVc(cores, ncolors)

model = ConcreteModel()

# Variáveis
model.x = Var(V, domain=Binary)  # Variáveis para indicar se um vértice é selecionado
model.y = Var(E, domain=Binary)  # Variáveis para indicar se uma aresta é selecionada

# Função objetivo
model.obj = Objective(
    expr=sum(model.x[v] for v in V) - sum(model.y[uv] for uv in E), sense=minimize)

# Restrições

model.cons = ConstraintList()

for c in C:
  model.cons.add(sum(model.x[v] for v in Vc[c]) == M[c])

for uv in E:
  model.cons.add(model.y[uv] <= model.x[uv[0]])

for uv in E:
  model.cons.add(model.y[uv] <= model.x[uv[1]])

# Resolver o modelo
solver = SolverFactory("glpk")
solver.options['tmlim']= 15
results = solver.solve(model)

# Imprimir resultadosz
print('Status:', results.solver.status)
print('Termination condition:', results.solver.termination_condition)
if results.solver.termination_condition == TerminationCondition.optimal:
    print("Solução ótima:", model.obj(), "Motfis")
    print("Vértices selecionados:")
    verticesList = []
    arestasList = []
    for v in V:
        if model.x[v].value == 1:
            verticesList.append(v)
    print(verticesList)
    print("Arestas selecionadas:")
    for uv in E:
        if model.y[uv].value == 1:
            arestasList.append(uv)
    print(arestasList)