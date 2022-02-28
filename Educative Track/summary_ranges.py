def summaryRanges(nums):
    i= 0
    j = len(nums)-1
    li = []
    a = ""
    fl = 0
    while i <= j:
        s = nums[i]
        fl = 0
        if i == j:
            li.append(str(nums[j]))
            break
        while i+1 <= j and nums[i] == nums[i+1]-1:
            a = str(s) + "->" + str(nums[i+1])
            print(a)
            i += 1
            fl =1
        if fl == 1:
            li.append(a)
        else:
            li.append(nums[i])
        i += 1
    print(li)

#summaryRanges([0,1,2,4,5,7])
#summaryRanges([0,2,3,4,6,8,9])
summaryRanges([0,1,2,4,5,7])
