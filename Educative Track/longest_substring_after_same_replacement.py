#aabccbb and 2 gives output 5 because bbbbb

# def inputfunction(mystr,num):
#     win_start, maxLen, maxRepeat = 0,0,0
#     freqMap = {}

#     totalLen = len(mystr)
#     for win_end in range(totalLen):
#         rightChar = mystr[win_end]
#         if rightChar not in freqMap:
#             freqMap[rightChar] = 0
#         freqMap[rightChar] += 1
#         maxRepeat = max(maxRepeat,freqMap[rightChar])
    
#         if (win_end-win_start+1-maxRepeat) > num:
#             leftChar = mystr[win_start]
#             freqMap[leftChar] -= 1
#             win_start += 1
    
#         maxLen = max(maxLen,win_end-win_start+1)
#     return maxLen


# def inputfunction(mystr,k):
#     win_start,win_end = 0,0
#     maxlen = float("-inf")
#     hashmap = {}

#     for _ in range(len(mystr)):
#         cur = mystr[win_end]
#         if cur not in hashmap:
#             hashmap[cur] = 0
#         hashmap[cur] += 1
#         n = k

        
#         duphash = {cur:1} 
#         temp = win_start
#         while (n>0 and win_start < win_end):
#             pos = mystr[win_start]

#             if pos != cur:
#                 duphash[cur] += 1
#                 n -= 1
#             else:
#                 duphash[cur] += 1
#             win_start += 1
        
#         if win_start < win_end-1:
#             win_start = temp + 1 # 7
#         else:
#             win_start = temp
        
        
#         if len(duphash) == 1:
#             maxlen = max(maxlen,win_end-win_start+1)
#         win_end += 1
#     return maxlen

def inputfunction(mystr,k):
    win_start,win_end,maxlen = 0,0,0
    hashmap = {}
    maxRep = 0

    for _ in range(len(mystr)):
        right = mystr[win_end]
        if right not in hashmap:
            hashmap[right] = 0
        hashmap[right] += 1

        maxRep = max(maxRep,hashmap[right])

        if (win_end-win_start+1-maxRep) > k:
            left = mystr[win_start]
            hashmap[left] -= 1
            win_start += 1
       
        maxlen = max(maxlen,win_end-win_start+1)
        win_end += 1
    return maxlen

        

   
print(inputfunction("aabccbb",2))
print(inputfunction("abbcb",1))
print(inputfunction("abccde",1))



"""
    win_start,win_end = 0,0
    maxslide = 0
    while win_end < len(mystr):
        astr = mystr[win_end]
        for i in range(win_end,len(mystr)):
            if mystr[i] == astr:
                win_end += 1
                maxslide += 1
                maxslide = max(maxslide, win_end-win_start)
            elif mystr[i+num] == astr:
                maxslide += num
                num = 0
                win_end += maxslide
        win_start = win_end
    return maxslide
"""
