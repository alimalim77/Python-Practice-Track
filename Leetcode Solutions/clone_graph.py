class Node:
    def __init__(self, val = 'A', neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def cloneGraph(self, node):
        visited = []
        while len(visited) < len(node.neighbors):
            for i in node.neighbors:
                if i not in visited:
                    print(i.val)
                    visited.append(i)
        print(visited)

    

jenny = Node()
martha = Node()
alex = Node()
trevor = Node(2,[jenny,martha,alex])
trevor.cloneGraph(trevor.neighbors[0])
print(trevor.neighbors)

