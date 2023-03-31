def lcm(a,b):
    return a*b//gcd(a,b)

def gcd(a,b):
    m = 1
    for i in range(2,min(a,b)+1):
        if a%i ==0 and b%i==0:
            m = max(m,i)
    return m
        

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        l = lcm(p,q)
        right = True if l/q %2 == 1 else False
        top = True if l/p %2 == 1 else False
        
        if right and top:
            return 1
        elif not right and top:
            return 2
        else:
            return 0