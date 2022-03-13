def longestsub(mystr,k):
    s = set()
    win_start, win_end = 0,0
    win_str = ""
    max_len = float('inf')
    while win_end < len(mystr):
        win_str = mystr[win_end]
        if len(s) > k:
            win_start += 1
        elif len(s) <= k:
            max_len = win_end - win_start
        if win_str not in s:
            s.add(win_str)
        win_end += 1
    return max_len


print(longestsub('cbbebi',3))