def maxArray(num, k):
    # maxsum = [0]
    # for i in range(0,len(num)-k+1,1): #O(n)
    #     if sum(num[i:i+k]) > sum(maxsum): #O(n)
    #         maxsum = num[i:i+k] 
    # return maxsum
    win_start,win_end = 0,0
    totsum = 0
    maxNum = float("-inf")

    for i in range(0,len(num)):
        totsum += num[win_end]
        maxNum = max(maxNum,totsum)
        win_end += 1

        if win_end - win_start == k:
            totsum -= num[win_start]
            win_start += 1 
    print(maxNum)
     

print(maxArray([2,3,4,1,5],2)) #[3,4]
print(maxArray([2,1,5,1,3,2],3)) #[5,1,3]


"""
    li = list()
        maxnum = max(nums[0:k])
        li.append(maxnum)
        for i in range(k,len(nums),1):
            if nums[i] > maxnum:
                maxnum = nums[i]
            li.append(maxnum)
        return li
"""