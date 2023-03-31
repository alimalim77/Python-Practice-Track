from collections import defaultdict
def longestsub(mystr,k):
    s = defaultdict()
    win_start, win_end = 0,0
    max_len = float('-inf')

    for _ in range(len(mystr)):
        if mystr[win_end] not in s:
            s[mystr[win_end]] = 0
        s[mystr[win_end]] += 1
        
        while len(s) > k:
            if mystr[win_start] in s:
                s[mystr[win_start]] -= 1
            if s[mystr[win_start]] == 0:
                del s[mystr[win_start]]
            win_start += 1
        max_len = max(max_len,win_end-win_start+1)
        win_end += 1
    return max_len


print(longestsub('araaci',2)) #4
print(longestsub('araaci',1)) #2
print(longestsub('cbbebi',3)) #5