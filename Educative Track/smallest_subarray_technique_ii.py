def minSubArrayLen(nums, target):
    win_start,win_end = 0,0
    totsum = 0
    need = float("inf")

    for i in range(len(nums)):
        totsum += nums[win_end]

        while totsum >= target:
            need = min(need,win_end-win_start+1)
            totsum -= nums[win_start]
            win_start += 1
        win_end += 1
        #print(totsum)
    return need

print(minSubArrayLen([2,1,5,2,3,2],7)) #2
print(minSubArrayLen([2,1,5,2,8],7)) #1 
print(minSubArrayLen([3,4,1,1,6],8)) #3