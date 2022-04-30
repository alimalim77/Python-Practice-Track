#aabccbb and 2 gives output 5 because bbbbb

def inputfunction(mystr,num):
    win_start, maxLen, maxRepeat = 0,0,0
    freqMap = {}

    totalLen = len(mystr)
    for win_end in range(totalLen):
        rightChar = mystr[win_end]
        if rightChar not in freqMap:
            freqMap[rightChar] = 0
        freqMap[rightChar] += 1
        maxRepeat = max(maxRepeat,freqMap[rightChar])
    
        if (win_end-win_start+1-maxRepeat) > num:
            leftChar = mystr[win_start]
            freqMap[leftChar] -= 1
            win_start += 1
    
        maxLen = max(maxLen,win_end-win_start+1)
    return maxLen
   
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
