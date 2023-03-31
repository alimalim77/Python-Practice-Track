


def fun(arr):
    l,r = 0,0

    for i in range(len(arr)-1):
        if arr[i+1] < arr[i]:
            l = i
            break
    
    for i in range(len(arr)-1,0,-1):
        if arr[i] < arr[i-1]:
            r = i
            break

    maxi,mini = max(arr[l:r+1]),min(arr[l:r+1])
    for i in range(l):
        if arr[i] > mini:
            l = i
            break
    for i in range(len(arr)-1,r,-1):
        if arr[i] < maxi:
            r = i
            break
    return r-l+1
        


print(fun([1,2,5,3,7,10,9,12])) #5
print(fun([1, 3, 2, 0, -1, 7, 10])) # 5

        

