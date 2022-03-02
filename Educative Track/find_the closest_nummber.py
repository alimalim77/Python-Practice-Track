def binsearch(target,*nums):
    li = list(map(int,nums))
    i = 0 
    j =len(li)-1
    closest = float("inf")
    while i <= j:
        mid = (i + j)//2
        if li[mid] == target:
            index = mid
            break
        if mid-1 >= i:
            if abs(target-li[mid-1]) < closest:
                closest = abs(target-li[mid-1])
                index = mid -1
        if mid+1 <= j:
            if abs(target-li[mid+1]) < closest:
                closest = abs(target-li[mid-1])
                index = mid + 1
        if li[mid] > target:
            j = mid-1        
        if li[mid] < target:
            i = mid+1

    print(li[index])
            
    
binsearch(17,3,6,8,9,16,19,26,78)