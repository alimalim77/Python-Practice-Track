def dfs(graph, source,stack,visited):
    visited.add(source)
    print(source)
    while stack:
        cur = stack.pop()

        for i in graph[cur]:
            if i not in visited:
                stack.append(i)
                dfs(graph,i,stack,visited)
    return True
            

graph = {
    'a':['b','e'],
    'b':['a','c'],
    'c':['b','e','d'],
    'd':['c','e'],
    'e':['a','e','d'],

}
print(dfs(graph,'a',['a'],set()))