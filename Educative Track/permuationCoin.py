arr = [4,2,3,5,6]
def permutationCoin(totLen, target):
    if target == 0:
        return 1
    res = 0
    for i in range(totLen):
        if arr[i] > target:
            continue
        res += permutationCoin(totLen,target-arr[i])
    return res
        
print(permutationCoin(len(arr),7))