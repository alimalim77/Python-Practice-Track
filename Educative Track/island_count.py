def island_count(grid):
  count = 0
  i = len(grid)
  j = len(grid[0])
  visited = set()
  for r in range(i):
    for c in range(j):
      if explore(grid,r,c,visited):
        count += 1
  return count
        
def explore(grid,r,c,visited):
  
  if (not(0 < r < len(grid))) or (not(0<c<len(grid[0]))):
    return
  
  if (r,c) in visited:
    return 
  visited.add((r,c))
  
  explore(grid,r+1,c,visited)
  explore(grid,r-1,c,visited)
  explore(grid,r,c+1,visited)
  explore(grid,r,c-1,visited)
  
  return True

grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]


print(island_count(grid))