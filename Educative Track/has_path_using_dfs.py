def haspath(graph, source,destination):
    node = [source]
    while len(node) != 0:
        a = node.pop()
        if a == destination:
            return True
        print(a)
        for i in graph[a]:
            node.append(i)
    return False

graph = {
    'a':['b','c'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'e':[],
    'f':[]
}
print(haspath(graph,'a','e'))