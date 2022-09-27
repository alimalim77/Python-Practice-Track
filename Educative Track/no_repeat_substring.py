'''
Input: String="aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
'''


# from collections import Counter
# def norepeat(mystr):
#     se = set()
#     win_start = 0
#     win_end = 0
#     maxlen = float("-inf")
    
#     while win_end < len(mystr):
        
#         if mystr[win_end] not in se:
#             se.add(mystr[win_end])
#             win_end += 1
        
#         else:
#             win_start += 1
#             win_end = win_start
#             maxlen = max(len(se),maxlen)
#             se.clear()
#     return maxlen

#from collections import Counter
def norepeat(mystr):
    win_start, win_end = 0,0
    maxlen = float("-inf")
    s = {}

    for _ in range(len(mystr)):
        cur = mystr[win_end]
        if cur not in s:
            s[cur] = 1
        else:
            while s[cur] > 0:
                pos = mystr[win_start]
                s[pos] -= 1
                win_start += 1
            s[cur] = 1
        maxlen = max(maxlen,win_end-win_start+1)
        win_end += 1
    return maxlen




print(norepeat("aabccbb")) #3
print(norepeat("abccde")) #3 
print(norepeat("abbbb")) #2
