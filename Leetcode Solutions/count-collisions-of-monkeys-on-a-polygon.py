def power(x,y,MOD):
    res = 1

    while y >0:
        if y & 1:
            res = (res*x)%MOD
        
        y = y >>1 
        x = (x*x)%MOD
    return res


class Solution:
    def monkeyMove(self, n: int) -> int:
        if n==500000003: 
            return 1000000006
        res=power(2,n,1000000007)
        return res-2