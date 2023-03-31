#Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, 
# find the length of the longest contiguous subarray having all 1s.
def longestsubarray(arr,k):
    win_start,win_end = 0,0
    hashmap = {1:0}
    maxlen = float("-inf")
    maxRep = 0


    for win_end in range(len(arr)):
        if arr[win_end] == 1:
            hashmap[1] += 1

        maxRep = max(maxRep,hashmap[1])

        if win_end-win_start+1-maxRep > k:
            left = arr[win_start]
            if left == 1:
                hashmap[left] -= 1
            win_start += 1
        maxlen = max(maxlen,win_end-win_start+1)
    return maxlen
# 1st index win start is zero win end is zero, maxrep = 1,maxlen = 1
# 2nd index win start is zero win end is 1 maxrep =1, maxlen = 
print(longestsubarray([1,1,0,0,1,1],2)) #6
print(longestsubarray([0,1,0,0,1,1,0,1,1,0,0,1,1],3)) #9
