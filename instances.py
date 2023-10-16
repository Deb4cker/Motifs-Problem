import csv
import numpy as np 
#---------------------------------------------------------------# 
class vertice:
    vertices = {}

    def __init__(self, name):
        self.name = name
        self.edges = []

        if name not in vertice.vertices:
            vertice.vertices[name] = self

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

#-----------------------------------------------------------------------------------------------------------#

#ESTES VALORES SAO OS DAS COLUNAS DA TABELA 1 NA PAGINA 237 DO ARTIGO

#graph_________________________________________________________________________
# 1- numero TOTAL de vertices do grafo;
I_V_I = ...

# 2- numero de cores;
I_C_I = ...

# 3- numero de vertices com cores repetidas;
I_VM_I = ...

#motif_________________________________________________________________________
# 4- tamanho do motif, soma de todas as vezes que uma cor aparece no motif:
    #exemplo: o motif tem 1 amarelo, 2 vermelhos e 1 azul, logo o tamanho do motif é 4;
I_M_I = ...

# 5 - quantas cores tem no motif.
I_CM_I = ...

#----------------------------------------Generating the colors---------------------------------------------#
def generateColors(table):
    if table == 'dm.csv':
        length = 269
    elif table == 'hs.csv':
        length = 318
    elif table == 'sc.csv':
        length = 216
    else:
        exit()
    return np.array(list(range(length)))

#----------------------------------------Generating the Graph---------------------------------------------#
V = [] #vertices
E = [] #arestas
C = [] #cores

def generateGraph(table):
    global V 
    global E
    global I_V_I
    global I_C_I
    global I_VM_I
    global I_M_I
    global I_CM_I   
    
    with open(table, newline='', encoding='utf-8') as f:
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
        #1
        I_V_I = len(V)
        #2
        I_C_I = list(range(1, 270))
        #3
        I_VM_I = ...
        #4
        I_M_I = ...
        #5
        I_CM_I = ...

#----------------------------------------Generating the Motif---------------------------------------------#
def generateMotif(vertices, edges):
    return "nao sei como fazer isso ainda"