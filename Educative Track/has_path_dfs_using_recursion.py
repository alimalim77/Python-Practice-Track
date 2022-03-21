import itertools

def haspath(graph, node, source, destination):
    node = [source]
    ans = False
    for i in graph[source]:
        node.append(i)
        ans = haspath(graph,node,i,destination)
        a = node.pop()
        
        if a == destination:
            #print("Arrived at --", destination)
            return True
        
        print(a)
    
    if ans:
        return True
    return False


graph = {
    'a':['b','c'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'e':[],
    'f':[]
}


print(haspath(graph,[],'a','e'))
print(haspath(graph,[],'a','f'))
