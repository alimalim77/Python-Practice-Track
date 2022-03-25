from ctypes.wintypes import PSHORT

def shortest_path(edges, node_A, node_B):
    s = set()
    a = [x[1] for x in edges]
    b = [x[0] for x in edges]
    for i in a:
        s.add(i)
    for i in b:
        s.add(i)
    graph = {}
    for i in s:
        graph[i] = []
    for i in edges:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    minimum = float("inf")
    visited = set()
    
    for i in graph[node_A]:
        visited=set()
        visited.add(node_A)
        minimum = min(minimum,check(graph,i,node_B,visited))
    return minimum
    


def check(graph, node_A,node_B,visited,path = 1):
    ini = node_A
    visited.add(ini)
    if ini == node_B:
        return path
    for i in graph[ini]:
        if i not in visited:
            return check(graph,i,node_B,visited,path + 1)
    return 0

edges = [
  ['a', 'c'],
  ['a', 'b'],
  ['c', 'b'],
  ['c', 'd'],
  ['b', 'd'],
  ['e', 'd'],
  ['g', 'f']
]

print(shortest_path(edges, 'a', 'e')) # -> 3