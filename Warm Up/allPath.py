from collections import defaultdict
def dfs(visited,res,src,des,graph,ans):
    if src in visited:
        return False,ans
    if src == des:
        if res[-1] != des:
            res.append(des)
            ans.append(res)
        return True,ans
    visited.add(src)
    res.append(src)

    for node in graph[src]:
        res.append(node)
        if node == des or dfs(visited,res,node,des,graph,ans)[0]:
            ans.append(res)
        visited.remove(node)
        res.pop()
    return False,ans
    
graph = [[4,3,1],[3,2,4],[3],[4],[]]
adjList = defaultdict(list)
for i,j in enumerate(graph):
    for node in j:
        adjList[i].append(node)
last = len(graph)-1


ans = []
for node in graph[0]:
    ans = dfs(set(),[0],node,last,adjList,ans)[1]
print(ans)
