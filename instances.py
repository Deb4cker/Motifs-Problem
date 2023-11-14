import random

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
    
