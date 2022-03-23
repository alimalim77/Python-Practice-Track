
def undirected_path(edges,nodeA,nodeB):
    graph = {}
    for i in edges:
        graph[i[0]] = i[1]
        graph[i[1]] = i[0]
    return checkedge(graph,nodeA,nodeB)



def checkedge(graph,one,two):
    node = [one]
    visited = set()
    while len(node) != 0:
        a = node.pop(0)
        visited.add(a)
        if a == two:
            print("Edge Connected")
            return True
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

print(undirected_path(edges, 'm', 'o')) # -> True