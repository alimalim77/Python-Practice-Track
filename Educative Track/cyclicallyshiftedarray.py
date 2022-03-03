def cycshifted(num):
    i = 0
    j = len(num) - 1
    
    while i <= j:
        mid = (i+j)//2
        if mid == 0 and num[mid+1] > num[mid]:
            return mid,num[mid]
        if num[mid-1] > num[mid]:
            return mid,num[mid]
        if num[i] > num[mid]:
            j = mid-1
        elif num[j] < num[mid]:
            i = mid+1
        else:
            j = mid-1
        

print(cycshifted([6,1,2,3,4,5]))