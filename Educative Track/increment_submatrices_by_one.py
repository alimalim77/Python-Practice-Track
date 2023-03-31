from collections import defaultdict
def fun(n,queries):
    res = []
    rows = defaultdict(list)
    for r1,c1,r2,c2 in queries:
        rows[r1].append((1,c1,c2+1))
        rows[r2+1].append((-1,c1,c2+1))
    
    diff = [0]*(n+1)
    for i in range(n):
        for d,c1,c2 in rows[i]:
            diff[c1]+= d
            diff[c2]-= d 
        
        cur = 0 
        row = []
        for x in diff:
            cur += x 
            row.append(cur) 
        row.pop() 
        res.append(row) 
    return res
    
    


print(fun(3,[[1,1,2,2],[0,0,1,1]]))