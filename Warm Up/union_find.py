class UnionFind:
    def __init__(self,data) -> None:
        self.data = [i for i in range(data)]
    
    def union(self,x,y):
        if self.connection(x,y):
            return True
        conA = self.find(x)
        conB = self.find(y)

        while conB != self.data[conB]:
            conB = self.data[conB]
    
        self.data[conB] = conA

    def find(self,x):
        return self.data[x]
    
    def connection(self,x,y):
        return self.find(x) == self.find(y)


uf = UnionFind(10)
# 1-2-5-6-7 3-8-9 4
uf.union(1, 2)
uf.union(2, 5)
uf.union(5, 6)
uf.union(6, 7)
uf.union(3, 8)
uf.union(8, 9)
print(uf.connected(1, 5))  # true
print(uf.connected(5, 7))  # true
print(uf.connected(4, 9))  # false
# 1-2-5-6-7 3-8-9-4
uf.union(9, 4)
print(uf.connected(4, 9))  # true