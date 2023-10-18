from pyomo.environ import * 
import instances
from instances import *

# # Dados do problema

nvertex = int(input("Digite o número de vértices: "))
ncolors = int(input("Digite o número de cores: "))


V = generateVertex(nvertex)  # Conjunto de vértices
C = generateColors(ncolors)  # Conjunto de cores
E = generateEdges(V) # Conjunto de arestas
M = generateM(nvertex, ncolors)  # Dicionário com a multiplicidade de cada cor em C
Vc = generateVc(V, nvertex, ncolors)

model = ConcreteModel()

#Parâmetros 
model.M = Param(C)
model.nvertex = Param()
model.ncolors = Param()

# Variáveis
model.x = Var(V, domain=Binary)  # Variáveis para indicar se um vértice é selecionado
model.y = Var(E, domain=Binary)  # Variáveis para indicar se uma aresta é selecionada

# Função objetivo
model.obj = Objective(expr=sum(model.x[v] for v in V) - sum(model.y[uv] for uv in E), sense=minimize)

# Restrições
model.const = ConstraintList()

for c in C:
    model.const.add(sum(model.x[v] for v in Vc[c]) == M[c])
for uv in E:
    model.const.add(model.y[uv] <= model.x[uv[0]])
    model.const.add(model.y[uv] <= model.x[uv[1]])
for v in V:
    model.const.add(model.x[v] >= 0)
    model.const.add(model.x[v] <= 1)
for uv in E:
    model.const.add(model.y[uv] >= 0)
    model.const.add(model.y[uv] <= 1)
# Resolver o modelo
solver = SolverFactory('glpk')
results = solver.solve(model)

# Imprimir resultados
print('Status:', results.solver.status)
print('Termination condition:', results.solver.termination_condition)
if results.solver.termination_condition == TerminationCondition.optimal:
    print('Optimal solution cost:', model.obj())
    print('Vértices selecionados:')
    for v in V:
        if model.x[v].value == 1:
            print(v)
    print('Arestas selecionadas:')
    for uv in E:
        if model.y[uv].value == 1:
            print(uv)
