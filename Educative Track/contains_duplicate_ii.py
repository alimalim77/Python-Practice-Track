def containsNearbyDuplicate(nums, k):
    ht = {}
    flag = 0
    for i,j in enumerate(nums):
        if j not in ht:
            ht[j] = i
        elif i - ht[j] <= k:
            flag = 1
        else:
            ht[j] = i
    print(flag)
    return False

print(containsNearbyDuplicate([1,0,1,1], 1))