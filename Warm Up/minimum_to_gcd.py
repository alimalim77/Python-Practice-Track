from math import gcd


def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)

def fun(nums,k):
    n = len(nums)
    res = 0
    for i in range(n):
        l,r  = i,i

        one,two = 0,0
        while l >= 0 and gcd(nums[i],nums[l]) == k :
            one += 1
            l -= 1
        
        if one:
            two -= 1
        while r < n  and gcd(nums[i],nums[r]) == k:
            two += 1
            r += 1
        if one or two:
            if two <= 0:
                res += fact(one)
            else:
                res += fact(one) + fact(two)            
    return res

print(fun([9,3,1,2,6,3],3))
            