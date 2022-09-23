class UnionFind:
    def __init__(self,data) -> None:
        self.data = [i for i in range(data)]
    
    def union(self,x,y):
        if self.connection(self,x,y):
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

    