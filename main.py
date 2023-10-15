from pyomo.environ import * 
import instances
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