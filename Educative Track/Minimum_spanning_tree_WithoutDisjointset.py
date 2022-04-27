ht = {}
def distance(p,i):
    return abs(p[0]-i[0]) + abs(p[1]-i[1])

def graph(i,point):
    ht[i] = list()
    for p in point:
        if tuple(p) == i:
            ht[i].append(float("inf"))
            continue
        ht[i].append(distance(tuple(p),i))

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        for i in points:
            graph(tuple(i),points)
        final = []
        ctr = 0
        for i in ht:
            for k,j in enumerate(ht[i]):
                final.append((ctr,k,j))
            ctr += 1
        print(ht, "is the table")
        final.sort(key= lambda x:x[2])
        edges = len(points)
        visited = set()
        total  = 0
        i = final[0]
        #print(total)
        print(final)
        for i in final:
            if len(visited) == edges:
                break
            
            if i[0] not in visited or i[1] not in visited or :
                if i[2] == float("inf"): continue
                visited.add(i[1])
                visited.add(i[0])
                
                print(i)
                total += i[2]
        ht.clear()
        return total