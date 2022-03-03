def firstdup(num,target):
    i = 0
    j =len(num) - 1
    
    while i <= j:
        mid = (i+j)//2

        if num[mid] < target:
            i= mid + 1
        elif num[mid] > target:
            j = mid-1
        else:
            if mid - 1 < 0:
                return 0
            if num[mid-1] != target:
                return mid
            else:
                j = mid-1

    


print(firstdup([1,2,4,4,5,5,17,29],4))