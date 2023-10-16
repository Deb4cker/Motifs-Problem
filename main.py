from pyomo.environ import * 
import instances
# #---------------------main----------------------#
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
# #---------------------pyomo----------------------#


# # Dados do problema

V = instances.V  # Conjunto de vértices
E = instances.E  # Conjunto de arestas
C = list(range(1, 270))  # Conjunto de cores
m = 24  # Dicionário com a multiplicidade de cada cor em C
print(C)

model = ConcreteModel()

# Variáveis
model.x = Var(V, domain=Binary)  # Variáveis para indicar se um vértice é selecionado
model.y = Var(E, domain=Binary)  # Variáveis para indicar se uma aresta é selecionada

# Função objetivo
model.obj = Objective(expr=sum(model.x[v] for v in V) - sum(model.y[uv] for uv in E), sense=minimize)

# Restrições

model.cons = ConstraitList()

for c in C:
    model.cons.add(sum(model.x[v] for v in V) == m[c])

for uv in E:
    model.cons.add(model.y[uv] <= model.x[uv[0]])

for uv in E:
    model.cons.add(model.y[uv] <= model.x[uv[1]])

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

