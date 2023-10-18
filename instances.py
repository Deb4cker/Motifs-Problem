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

def generateM(nvertex,ncolors):
    m = []
    max = nvertex
    for i in range(ncolors):
        if(i == ncolors-1):
            m.append(max)
            break
        quantity = random.randint(0, max//2)
        m.append(quantity)
        max -= quantity
    return m

def generateVc(vertex, M, ncolors):
    vertexCopy = [x for x in vertex]
    # vc = [[]] * ncolors
    vc = []
    for i in range(ncolors):
        vc.append([])
        
    for i,m in enumerate(M):
        for j in range(m):
            v = random.choice(vertexCopy)
            vc[i].append(v)
            vertexCopy.remove(v)
    return vc
