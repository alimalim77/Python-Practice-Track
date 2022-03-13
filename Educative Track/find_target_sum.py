def findTargetSumWays(nums, target):
    dp = {}
        
    def backtrack(index,total):
        if len(nums) == index:
            return 1 if total==target else 0
            
        if (index,total) in dp:
            return dp[(index,total)]
        dp[(index,total)] = (backtrack(index+1,total+nums[index]) + backtrack(index+1,total-nums[index]))
        return dp[(index,total)]
    return backtrack(0,0)

print(findTargetSumWays([1,1,1,1,1],3))