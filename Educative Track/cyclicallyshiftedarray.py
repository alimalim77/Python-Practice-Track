def cycshifted(num):
    i = 0
    j = len(num) - 1
    
    while i <= j:
        mid = (i+j)//2
        if num[j] < num[mid]:
            i = mid+1
        elif num[i] < num[mid]:
            j = mid-1
        else:
            return mid

print(cycshifted([3,4,5,6,7,1,2]))