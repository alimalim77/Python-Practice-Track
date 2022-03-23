
def undirected_path(edges,nodeA,nodeB):
    starting_nodes = [x[0] for x in edges]
    con_nodes = [x[1] for x in edges]
    s = set(starting_nodes).union(set(con_nodes))
    graph = {}
    
    for i in s:
        graph[i] = []
    for i in edges:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    print(graph)
    return checkedge(graph,nodeA,nodeB)



def checkedge(graph,one,two):
    node = [one]
    visited = set()
    while len(node) != 0:
        a = node.pop(0)
        if a == two:
            print("Node Found")
            return True
        visited.add(a[0])
        for i in graph[a]:
            if i not in visited:
                node.append(i)
    return False
        

edges = [
  ('i', 'j'),
  ('k', 'i'),
  ('m', 'k'),
  ('k', 'l'),
  ('o', 'n')
]

print(undirected_path(edges, 'm', 'j')) # -> True