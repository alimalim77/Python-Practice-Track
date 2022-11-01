def fun(creators,ids,views):
    creatorHashmap = {}
    for i,j in zip(creators,views):
        if i not in creatorHashmap:
            creatorHashmap[i] = 0
        creatorHashmap[i] += j
    largest = max(creatorHashmap.values())
    creatorList = {}
    for name,view in creatorHashmap.items():
        if view == largest:
            creatorList[name] = 0
        
    viewmap = {}
    for i,j,k in zip(creators,views,ids):
        if i in creatorList:
                #creatorList[i] = max(j,creatorList[i])
            if j > creatorList[i]:
                creatorList[i] = j
                viewmap[i] = k
        
                    
                
    res = []
    for i,j in viewmap.items():
        res.append([i,j])
    return res


print(fun(["a"],["a"],[0]))
