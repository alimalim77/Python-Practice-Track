def maxArray(num, k):
    maxsum = [0]
    for i in range(0,len(num)-k+1,1):
        if sum(num[i:i+k]) > sum(maxsum):
            maxsum = num[i:i+k]
    return maxsum

print(maxArray([2,1,5,1,3,2],3))