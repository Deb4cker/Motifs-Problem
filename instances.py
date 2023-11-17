import random

class Motif:
    def __init__(self, subgraph):
        self.subgraph = subgraph
        self.notConnectedEdges = len(subgraph) * (len(subgraph) - 1) // 2 - len(subgraph)

def generateVertex(nvertex):
    vertex = []
    for i in range(nvertex):
        vertex.append(i)
    return vertex

def generateColors(ncolors):
    colors = []
    for i in range(ncolors):
        colors.append(i)
    return colors

def generateEdges(vertex):
    vertexCopy = [x for x in vertex]
    pumEdges = []
    while len(vertexCopy) > 1:
        v = random.choice(vertexCopy)
        vertexCopy.remove(v)
        u = random.choice(vertexCopy)
        pumEdges.append((v, u))
    return pumEdges

def generateVerticesColors(V, ncolors):
    vertexColor = [0 for _ in range(len(V))]
    for i in range(len(vertexColor)):
        vertexColor[i] = random.randint(0, ncolors - 1)
    return vertexColor    

def generateM(ncolors, cores):
    m = []
    for c in range(ncolors):
        amount = len([x for x in cores if x == c])
        m.append(random.randint(0, amount))
    return m

def generateVc(cores, ncolors):
    Vc = {}
    for c in range(ncolors):
        Vc[c] = []
        for i in range(len(cores)):
            if cores[i] == c:
                Vc[c].append(i)
    return Vc

def generateSolution(vertex):
    solution = [0 for _ in range(len(vertex))]
    return solution

def countEdges(vertex, edges):
    solution = [0 for _ in range(len(vertex))]
    for i in range(len(edges)):
        solution[edges[i][0]] += 1
        solution[edges[i][1]] += 1
    return solution

def getConnectedVertices(vertex, edges, v):
    connectedVertices = []
    for i in range(len(edges)):
        if edges[i][0] == v:
            connectedVertices.append(edges[i][1])
        elif edges[i][1] == v:
            connectedVertices.append(edges[i][0])
    return connectedVertices

def getColorsOfVertices(vertex, vertexColor):
    colors = {}
    for v in vertex:
        for color, vertices in vertexColor.items():
            if v in vertices:
                colors[v] = color
                break
    return colors

def getVerticeColor(vertice, vertexColor):
    for color, vertex in vertexColor.items():
        if vertice in vertex:
            return color

def countColorByM(vertice, color, M, countArray, possibleSolution):
    if M[color] > countArray[color]:
        countArray[color] = countArray[color] + 1
        possibleSolution.append(vertice)


def verticeVisited(v, visitedVerticesArray):
    visitedVerticesArray[v - 1] = True


def getRandomNotVisitedVertice(visitedVerticesArray):
    notVisitedVertex = [i for i, visited in enumerate(visitedVerticesArray) if not visited]
    return random.choice(notVisitedVertex)

def solve(Vertex, Edges, Vc, randomVertice, M):
    countArray = [0 for _ in range(len(M))]               # Array de contagem de cores. Conta quantas vezes uma cor foi usada 
    visitedVertices = [False for _ in range(len(Vertex))] # Array de vértices visitados
    possibleSolution = []                                 # Array de solução possível
    
    countColorByM(randomVertice, getVerticeColor(randomVertice, Vc), M, countArray) #vai contabilizar a cor do vertice aleatorio

    while M != countArray:                                                  # Enquanto o array de contagem de cores for diferente do array de cores
        connectedVertices = getConnectedVertices(Edges, randomVertice)      # Pega os vértices conectados ao vértice aleatório
        for v in connectedVertices:                                         # Para cada vértice conectado
            vColor = getVerticeColor(v, Vc)                                 # Pega a cor do vértice
            countColorByM(v, vColor, M, countArray, possibleSolution)       # Contabiliza a cor do vértice (se for possível)
        verticeVisited(v, visitedVertices)                                  # Marca o vértice como visitado (nesta iteração)
        randomVertice = getRandomNotVisitedVertice(Vertex, visitedVertices) # Pega um vértice aleatório não visitado
