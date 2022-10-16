nums = [1,2,3,4,5]
change = 0
for i in range(len(nums)-1,0,-1):
    if nums[i-1] < nums[i]:
        change += 1
if change == 0:
    print(False)


for i in range(len(nums)):
    l,r = i+1,len(nums)
    res = []
    for j in range(l,r):
        if nums[j] > nums[i]:
            res.append(nums[j])

    if len(res) > 1:
        for j in range(1,len(res)):
            if res[j] > res[j-1]:
                print(True)