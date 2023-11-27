import random

def start(degrees, graph, verticeSet, Vc, M):
    initial_vertex = [get_greater_degree_with_desired_color(degrees, Vc, M)]
    vertexes = iterated_greedy(initial_vertex, graph, verticeSet, Vc, M, degrees)
    return vertexes

def iterated_greedy(initial_vertex, graph, verticeSet, Vc, M, degrees):
    S_incumbent = construction(initial_vertex, graph, verticeSet, Vc, M, degrees)
    S = S_incumbent.copy()
    stagnation = 100
    while stagnation > 0:
        S = destruction(S)
        S = construction(S, graph, verticeSet, Vc, M, degrees)
        if sumDeltas(graph, S, verticeSet) < sumDeltas(graph, S_incumbent, verticeSet):
            S_incumbent = S
            stagnation = 100
        else:
            stagnation -= 1

    return S_incumbent

def destruction(solution):
    S = solution.copy()
    number_of_s_to_be_removed = int(len(S) / 2)
    for _ in range(number_of_s_to_be_removed):
        s = random.choice(S) 
        index = S.index(s)
        S.pop(index)
            
    return S

def construction(solution, graph, verticeSet, Vc, M, degrees):
    S = solution.copy()
    countColors = generateCountColors(S, Vc)
    
    while countColors != M:
        deltas = strategy(graph, S, verticeSet, Vc, M, countColors)
        candidates = select_candidates(deltas)
        s = chooseSGreedy(degrees, candidates, deltas)
        addColor(s, countColors, Vc)
        if s not in S: S.append(s)

    return S

def strategy(graph, S, verticeSet, Vc, M, countColors):
    queue = [x for x in graph.get(S[0])]
    deltas = calculate_delta(queue, graph, S, verticeSet)
    deltas = removeSVertexFromDelta(S, deltas)
    deltas = removeNonNecessaryColors(Vc, M, countColors, deltas,S)
    if len(deltas) == 0:
        print('aqui')
    organized_deltas = sortDeltas(deltas)
    return organized_deltas

def generateCountColors(S, Vc):
    countColors = [0 for _ in range(len(Vc))]
    for s in S:
        addColor(s, countColors, Vc)
    return countColors


def addColor(s, colorCount, Vc):
    for color, vertex in Vc.items():
        for v in vertex:
            if v == s:
                colorCount[color] += 1


def calculate_delta(queue, graph_original, S, verticeSet):
    graph = graph_original.copy()
    visited = []
    current_delta = [{x: 0} for x in verticeSet]

    while len(queue) != 0:
        s = queue[0]
        for neighbor in graph.get(s):
            if neighbor not in visited:
                if s in S:
                    n_neighbor_in_s = sum(el in graph.get(neighbor) for el in S)
                    current_delta[neighbor] = {neighbor: (1 - n_neighbor_in_s)}
                else:
                    if current_delta[s].get(s) < 0:
                        current_delta[neighbor] = {neighbor: 1}
                    elif neighbor in S:
                        current_delta[neighbor] = {neighbor: 0}
                    else:
                        current_delta[neighbor] = {
                            neighbor: current_delta[s].get(s) + 1
                        }        
                queue.append(neighbor)
                visited.append(neighbor)
                                        
        queue.pop(0)

    return current_delta

def removeSVertexFromDelta(S, deltas):
    deltas =  [d for d in deltas if list(d.keys())[0] not in S]
    return deltas

def removeNonNecessaryColors(Vc, M, colorCount, deltas,S):
    delta_vertexes = []
    vertexes_to_be_removed = []
    
    for delta_dict in deltas:
        for key in delta_dict:
            delta_vertexes.append(key)
            
    for i in range(len(M)):
        for vertex_key in delta_vertexes:
            if vertex_key in Vc.get(i):
                if colorCount[i] == M[i]:
                    vertexes_to_be_removed.append(vertex_key)
    deltas = deltas.copy()
    deltas = [d for d in deltas if list(d.keys())[0] not in vertexes_to_be_removed]
    
    return deltas

def sortDeltas(delta):
    delta_copy = [x for x in delta]
    return sorted(delta_copy, key=lambda x: list(x.values())[0])


def select_candidates(deltas):
    k = 0.5
    numberOfCandidates = int(len(deltas) * k)
    deltas_copy = [x for x in deltas]
    candidates = []

    if numberOfCandidates > 0:
        for i in range(numberOfCandidates):
            candidates.append(list(deltas_copy[i].keys())[0]) 
    else:
        candidates.append(list(deltas_copy[0].keys())[0])
    return candidates

def chooseSGreedy(degrees, candidates, deltas):
    return random.choice(candidates)

def deltaIsGreaterOrEqual(candidate, best_candidate, deltas):
    delta_dict = {key: value for d in deltas for key, value in d.items()}

    return delta_dict.get(candidate) >= delta_dict.get(best_candidate)

def sumDeltas(graph, S, verticeSet):
    sum = 0
    queue = graph.get(S[0])
    deltas = calculate_delta(queue, graph, S, verticeSet)
    for s in S:
        sum += deltas[s].get(s)
    return sum    
    

def countDegrees(graph, V):
    grades = [0 for _ in range(len(V))]
    for v in V:
        grades[v] = len(graph.get(v))
    return grades

def get_greater_degree_with_desired_color(degrees, Vc, M):
    not_desired_colors = []
    for i in range(len(M)):
        if M[i] == 0:
            not_desired_colors.extend(Vc.get(i))
            
    for index, _ in enumerate(degrees):
        if index in not_desired_colors:
             degrees[index] = 0
    return degrees.index(max(degrees))
