def largest_component(graph):
  visited = set()
  maximum = float("-inf")
  for i in graph:
    maximum = max(maximum,explore(graph,i,visited,0))
  return maximum

def explore(graph, ini, visited,maximum):
  node = [ini]
  while len(node) != 0:
    a = node.pop(0)
    if a in visited:
        continue
    visited.add(a)
    maximum += 1
    for i in graph[a]:
      if i not in node:
        node.append(i)
  return maximum
     
#TestCase 1
print(largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}))# -> 4


#TestCase 2
print(largest_component({
  1: [2],
  2: [1,8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
})) # -> 6

#Testcase 3
print(largest_component({
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
})) # -> 5