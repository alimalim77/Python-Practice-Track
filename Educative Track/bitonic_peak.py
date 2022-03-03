


def bitonicpeak(num):
    i = 0
    j =len(num) - 1
    mid = (i+j)//2
    mid_left = mid-1
    mid_right= mid +1

    while i <= j:
        if mid_left < 0:
            return
        if mid_right > len(num)-1:
            return 
        if num[mid_left] < num[mid] and num[mid] > num[mid_right]:
            return num[mid]
        if num[mid_left] < num[mid] and num[mid] < num[mid_right]:
            i = mid+1
            mid = (i+j)//2
            mid_left = mid-1
            mid_right= mid +1
        if num[mid_left] > num[mid] and num[mid] > num[mid_right]:
            j = mid-1
            mid = (i+j)//2
            mid_left = mid-1
            mid_right= mid +1     
    return False   


print(bitonicpeak([1,2,3,4,5,4,2,1]))