import math
def countPrimes(n) :
        if n < 2:
            return 0
        store = [True] * n
        store[0],store[1] = False, False
        a = int(math.ceil(math.sqrt(n)))
        
        for i in range(2,a):
            if store[i]:
                for j in range(i*i,n,i):
                    print(j)
                    store[j] = False
        #return list(enumerate(store))
    
print(countPrimes(34))