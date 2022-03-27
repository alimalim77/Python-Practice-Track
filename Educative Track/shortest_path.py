from collections import deque
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
    visited = set([node_A])
    queue = deque([(node_A,0)])
    
    while queue:
        node, distance = queue.popleft()

        if node == node_B:
            return distance
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor,distance+1))
    return -1
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