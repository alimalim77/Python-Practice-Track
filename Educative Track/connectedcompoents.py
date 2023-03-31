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


def graphMaker(edges,n):
    for i in range(n):
        graph[i] = []

    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)
    

if __name__ == "__main__":
    n = 7
    edges = [[1,2],[3,4],[4,5],[6,3],[6,4]]
    graph = {}
    graphMaker(edges,n)
    ans = connectedcomponents(graph)
    print(ans)


# Using Union Find
class UnionFind:
    # Constructor of Union-find. The size is the length of the root array.
    def __init__(self, size):
        self.root = [i for i in range(size)]
        
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.root[rootY] = rootX
        
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        nodes = defaultdict(list)
        for i,j in edges:
            nodes[i].append(j)
        obj = UnionFind(n)
        for edge in nodes.keys():
            for trav in nodes[edge]:
                obj.union(edge,trav)
        count = 0
        for i,j in enumerate(obj.root):
            if i == j:
                count += 1
        return count

