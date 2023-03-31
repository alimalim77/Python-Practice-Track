def maxsum(arr,k):
    res = 0
    n = len(arr)
    maxs = [0]*n

    current = arr[0]
    maxs[0] = current
    for i in range(1,n):
        if current > 0:
            current += arr[i]
        else:
            current = arr[i]
        maxs[i] = current
    
    exact = 0
    for i in range(k):
        exact += arr[i]
    if exact > res:
        res = exact
    
    for i in range(k,n):
        exact = arr[i] - arr[i-k]
        if exact > res:
            res = exact 
        win = maxs[i-k] + exact
        if win > ans:
            ans = win 
    return ans
    


print(maxsum([],))