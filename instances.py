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

def generateGraph(vertex, edges):
    graph = {}
    for v in vertex:
        graph[v] = []
    for edge in edges:
        v1, v2 = edge
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph

def generateVerticesWithColors(vertexColor, V):
    verticesWithColors = [0 for _ in range(len(V))]
    for color, vertices in vertexColor.items():
        for vertice in vertices:
            verticesWithColors[vertice] = color
    return verticesWithColors

def generateGraph(vertex, edges):
    graph = {}
    for v in vertex:
        graph[v] = []
    for edge in edges:
        v1, v2 = edge
        graph[v1].append(v2)
        graph[v2].append(v1)
    return graph

def getVerticeColor(vertex, dicitonary):
    return dicitonary[vertex]

def getGrade(grades, vertex):
    return grades[vertex]

def generateGrades(graph, V):
    grades = [0 for _ in range(len(V))]
    for vertex in graph:
        grades[vertex] = len(graph[vertex])
        
def depth_search(queue, graph, S, V):
    visited = []
    current_delta = [0 for _ in range(len(V))]
    
    while len(queue) != 0:
        s = queue[0]
        if s not in S:
            for neighbor in graph.get(s):
                if neighbor in S and neighbor not in visited                   :
                    n_neighbor_in_s = sum(el in graph.get(s) for el in S)
                    current_delta[s] = (1 - n_neighbor_in_s)
                elif neighbor not in visited:
                    if current_delta[s] < 0:
                        current_delta[neighbor] = 1
                    else:
                        current_delta[neighbor] = current_delta[s] + 1
                
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
            
        queue.pop(0)
        visited.append(s)
            
            
    return current_delta
