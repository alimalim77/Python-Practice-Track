arr = [4,2,3,5,6]
def combinationCoin(length,totLen, target):
    if target == 0:
        return 1
    res = 0
    for i in range(length,totLen):
        if arr[i] > target:
            continue
        res += combinationCoin(i+1, totLen,target-arr[i])
    return res
        
print(combinationCoin(0,len(arr),7))