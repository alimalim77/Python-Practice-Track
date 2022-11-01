def connectedcomponents(graph):
    visited = set()
    count = 0

    for node in graph:
        if node not in visited and dfs(graph,node,visited):
            count += 1
    return count
    


def dfs(graph,node,visited):
    visited.add(node)

    for nextNode in graph[node]:
        if nextNode not in visited:
            dfs(graph,nextNode,visited)
    return True


def graphMaker(edges):
    for a,b in edges:
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
        if b not in graph:
            graph[b] = [a]
        else:
            graph[b].append(a)
    

if __name__ == "__main__":
    edges = [[1,2],[3,4],[4,5],[6,3],[6,4]]
    graph = {}
    graphMaker(edges)
    ans = connectedcomponents(graph)
    print(ans)

