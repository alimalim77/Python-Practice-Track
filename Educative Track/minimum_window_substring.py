def checker(have, need):
    for i in need.keys():
        if have[i] > need[i]:
            return False
    return True

def checkertwo(have, need):
    for i in need.keys():
        if have[i] < need[i]:
            return False
    return True

def minWindow(s, t):
    need, have = {} , {}
    for i in t:
        if i not in need:
            need[i] = 1
        else:
            need[i] += 1
        
    for i in need.keys():
        have[i] = 0
        
    print(have)
    print(need)
        
    maxLen = float("inf")
    win_start = 0
    i = 0 
    j=0
    while i < len(s):
        i = win_start
        while j < len(s) and checker(have,need):
            if s[j] in have:
                have[s[j]] += 1
            j += 1
        else:
            if win_start >= len(s):
                return maxLen
            if s[win_start] in have:
                have[s[win_start]] -= 1
            win_start += 1
        if checkertwo(have,need):
            maxLen = min(maxLen,j-win_start)
    return maxLen

print(minWindow("ADOBECODEBANC","ABC"))