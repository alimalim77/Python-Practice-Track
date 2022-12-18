import math
def primeFactors(n):
    res = []
    while n % 2 == 0:
        res.append(2)
        n //= 2
    
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i == 0:
            res.append(i)
            n //= i
    if n > 2:
        res.append(n)
    return res
    
def smallestValue(n):
    while True:
        facTuples = primeFactors(n)
        if len(facTuples) == 1:
            return facTuples[0]
        n = sum(facTuples)
        if n == org:
            return n
    
print(smallestValue(4)) #5
print(smallestValue(3)) #3
            