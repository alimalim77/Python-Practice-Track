
def connected_components_count(graph):
    visited = set()
    ctr = 0
    for i in graph:
        if explore(graph,i,visited):
            ctr += 1
        #print("Ctr incremented by", ctr)
    return ctr

def explore(graph,initial,visited):
    
    if initial in visited:
        return False
    visited.add(initial)
    
    for i in graph[initial]:
        explore(graph,i,visited)
        
    return True


#TestCase 1
print(connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
})) # -> 5


#TestCase 2
print(connected_components_count({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
})) # -> 1


#-----------3/5 Test Cases Passed-------------------
"""
def connected_components_count(graph):
    visited = set()
    ctr = 0
    for i in graph:
        if explore(graph,i,visited):
            ctr += 1
        #print("Ctr incremented by", ctr)
    return ctr

def explore(graph,initial,visited):
    node = [initial]
    a = node.pop()
    if a in visited:
        return False
    visited.add(a)
    
    for i in graph[a]:
        if i not in visited:
            node.append(i)
            return explore(graph,i,visited)
        
    if len(node) == 0 and len(visited) < len(graph):
        return True
    else:
        return False
"""