def singleNumber(nums):
    ans=0
    for i in nums:
        ans = ans ^i
    return ans

print(singleNumber([4,1,2,1,2,7,6]))