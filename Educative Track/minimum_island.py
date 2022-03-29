
def minimum_island(grid):
  mini = float("inf")
  i = len(grid)
  j = len(grid[0])
  visited = set()
  for r in range(i):
    for c in range(j):
      minimum = explore(grid,r,c,visited)
      if minimum > 0 and minimum < mini:
          mini = minimum
  return mini
        
def explore(grid,r,c,visited):
  if not(0 <= r < len(grid)) or (not(0 <= c < len(grid[0]))):
    return 0
  if grid[r][c] == 'W':
      return 0
  
  
  if (r,c) in visited:
    return 0
  visited.add((r,c))
  
  path = 1
  path += explore(grid,r+1,c,visited)
  path += explore(grid,r-1,c,visited)
  path += explore(grid,r,c+1,visited)
  path += explore(grid,r,c-1,visited)
  
  return path

grid = [
  ['L', 'W', 'W', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'L', 'W'],
  ['W', 'W', 'W', 'W', 'W'],
  ['W', 'W', 'L', 'L', 'L'],
]

print(minimum_island(grid)) # -> 2