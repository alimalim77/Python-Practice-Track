def findDuplicate(nums):
    turtle = 0
    hare = 0
    while True:
        if turtle >= len(nums):
            turtle = 0
        if hare >= len(nums):
            hare = 0
        if nums[turtle] == nums[hare] and turtle != hare:
            return nums[turtle]
        turtle += 1
        hare += 2
    return None
print(findDuplicate([1,4,2,4,2]))