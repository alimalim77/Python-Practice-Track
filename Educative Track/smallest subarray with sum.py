"""
def smallestsub(num,k):
    for i in range(1, len(num)+1):
        for j in range(0,len(num)-i+1,1):
            print(num[j:j+i])
            if sum(num[j:j+i]) >= k:
                return len(num[j:j+i])


print(smallestsub([1,2,3,4,5],15))
"""
#18/19 Cases Passed : TLE Error

#Approach No. 2
def minSubArrayLen(nums, target):
        win_start, win_end = 0,0
        win_sum = 0
        min_len = float('inf')
        
        while win_end != len(nums):
            win_sum += nums[win_end]
            if win_sum > target:
                min_len = min(min_len,win_end - win_start-1)
                win_sum -= nums[win_start]
                win_start += 1
                continue
            
            win_sum += nums[win_end]
            win_end += 1 
        if min_len == float("inf")
        return min_len
    

print(minSubArrayLen([2,1,5,2,3,2],7))

#Approach 3
# Is hould have used 
'''
      win_start, win_end = 0,0
        win_sum = 0
        min_len = float('inf')
        
        while win_end < len(nums):
            win_sum += nums[win_end]
            while win_sum >= target:
                min_len = min(min_len,win_end - win_start+1)
                win_sum -= nums[win_start]
                win_start += 1
            
            win_end += 1
        if min_len == float('inf'):
            return 0
        return min_len
'''