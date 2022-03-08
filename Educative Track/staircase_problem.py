'''

a = 0
def stair(n,ctr = 0, m =2):
    if n == 0:
        return
    if n == ctr:
        return 1 + stair(n,ctr+1)
    if n < ctr:
        return

    for i in range(1,m+1):
        return stair(n,ctr+i)
        

print(stair(4))
'''

def staircase(n, m):
 
  if n == 0:    
    return 1
  ways = 0
  
  for i in range(1,m+1):  
    if i <= n:          
      ways += staircase(n-i, m) 
  return ways

print(staircase(4,2))