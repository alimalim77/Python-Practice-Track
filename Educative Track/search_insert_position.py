def bindup(nums,target,start,end):
    mid = (start+end)//2
    if nums[mid] < target and nums[mid+1] < target:
        return bindup(nums,target,mid+1,end)
    elif nums[mid] > target and nums[mid-1] > target:
        return bindup(nums,target,start,mid+1)
    else:
        if nums[mid] < target:
            return mid + 1
        return mid
    return None

def binarysearch(nums,target,start,end):
    if start > end : return None
    mid = (start+end)//2
    if nums[mid] < target:
        return binarysearch(nums,target,mid+1,end)
    elif nums[mid] > target:
        return binarysearch(nums,target,start,mid-1)
    elif nums[mid] == target:
        return mid
    return None


def searchInsert(nums, target):
    a = binarysearch(nums,target,0,len(nums)-1)
    if a != None:
        return a
    else:
        if target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        else:
            return bindup(nums,target,0,len(nums)-1)


print(searchInsert([1,3,5],4))