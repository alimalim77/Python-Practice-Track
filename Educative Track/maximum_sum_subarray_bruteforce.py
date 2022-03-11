def maxArray(num, k):
    maxsum = [0]
    for i in range(0,len(num)-k+1,1):
        if sum(num[i:i+k]) > sum(maxsum):
            maxsum = num[i:i+k]
    return maxsum

print(maxArray([2,3,4,1,5],2))


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