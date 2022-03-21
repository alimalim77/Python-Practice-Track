def haspath(graph, source):
    node = [source]
    while len(node) != 0:
        a = node.pop(0)
        print(a)
        for i in graph[a]:
            node.append(i)

graph = {
    'a':['b','c'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'e':[],
    'f':[]
}
haspath(graph,'a')