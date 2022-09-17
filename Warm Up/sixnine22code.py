def fun(arr):
    curmax = 1
    globalmax = float("-inf")

    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            curmax += 1
        else:
            curmax = 0
        globalmax = max(globalmax,curmax)
            

    return len(arr)-globalmax
    

print(fun([3,4,5,6,7,8,1]))