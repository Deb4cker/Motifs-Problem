import random

def start(degrees, graph, verticeSet, Vc, M):
    initial_vertex = [get_greater_degree_with_desired_color(degrees, Vc, M)]
    vertexes = iterated_greedy(initial_vertex, graph, verticeSet, Vc, M)
    return vertexes

def iterated_greedy(initial_vertex, graph, verticeSet, Vc, M):
    S_incumbent = construction(initial_vertex, graph, verticeSet, Vc, M)
    S = S_incumbent.copy()
    stagnation = 100
    while stagnation > 0:
        S = destruction(S)
        S = construction(S, graph, verticeSet, Vc, M)
        if count_connected_components(graph, S) < count_connected_components(graph, S_incumbent):
            S_incumbent = S
            stagnation = 100
        else:
            stagnation -= 1

    return S_incumbent, count_connected_components(graph, S_incumbent) 

def destruction(solution):
    k = 0.5
    S = solution.copy()
    number_of_s_to_be_removed = int(len(S) * k)
    for _ in range(number_of_s_to_be_removed):
        s = random.choice(S) 
        index = S.index(s)
        S.pop(index)
            
    return S

def construction(solution, graph, verticeSet, Vc, M):
    S = solution.copy()
    countColors = generateCountColors(S, Vc)
    
    while countColors != M:
        deltas = strategy(graph, S, verticeSet, Vc, M, countColors)
        candidates = select_candidates(deltas)
        s = chooseS(candidates)
        addColor(s, countColors, Vc)
        if s not in S: S.append(s)

    return S

def strategy(graph, S, verticeSet, Vc, M, countColors):
    queue = [x for x in graph.get(S[0])]
    deltas = calculate_delta(queue, graph, S, verticeSet)
    deltas = removeSVertexFromDelta(S, deltas)
    deltas = removeNonNecessaryColors(Vc, M, countColors, deltas,S)
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
        q = queue[0]
        for neighbor in graph.get(q):
            if neighbor not in visited:
                if neighbor in S:
                        current_delta[neighbor] = {neighbor: 0}
                elif sum(el in graph.get(neighbor) for el in S) > 0: #if neighbor contains another neighbor in S
                    n_neighbor_in_s = sum(el in graph.get(neighbor) for el in S)
                    current_delta[neighbor] = {neighbor: (1 - n_neighbor_in_s)}
                else:
                    if current_delta[q].get(q) < 0:
                        current_delta[neighbor] = {neighbor: 1}
                    else:
                        current_delta[neighbor] = {
                            neighbor: current_delta[q].get(q) + 1
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
    return sorted(delta_copy, key=lambda x: (list(x.values())[0], list(x.keys())[0]))


def select_candidates(deltas):
    k = 0.2
    numberOfCandidates = int(len(deltas) * k)
    deltas_copy = [x for x in deltas]
    candidates = []

    if numberOfCandidates > 0:
        for i in range(numberOfCandidates):
            candidates.append(list(deltas_copy[i].keys())[0]) 
    else:
        candidates.append(list(deltas_copy[0].keys())[0])
    return candidates

def chooseS(candidates):
    return random.choice(candidates)

def deltaIsGreaterOrEqual(candidate, best_candidate, deltas):
    delta_dict = {key: value for d in deltas for key, value in d.items()}

    return delta_dict.get(candidate) >= delta_dict.get(best_candidate)

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

def count_connected_components(graph, S):
    visited = {s: False for s in S}
    count = 0
    index = check_graph_is_visited(visited)
    while index != -1:
        dfs(graph, index, visited)
        count += 1
        index = check_graph_is_visited(visited)
    return count

def check_graph_is_visited(visited):
    for key in visited:
        if not visited.get(key):
            return key
    return -1

def dfs(graph, start, visited):
    if visited.get(start) == None:
        return
 
    visited[start] = True
    
    for destination in graph.get(start):
        if not visited.get(destination):
            dfs(graph, destination, visited)
            