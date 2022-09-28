def smallest_window(mystr,pattern):
    finstring = ""
    matched = 0
    win_start,win_end = 0,0
    hashmap = {}
    maxlen = float("inf")
    for i in pattern:
        if i not in hashmap:
            matched += 1
            hashmap[i] = 0
        hashmap[i] += 1
    
    
    for win_end in range(len(mystr)):
        right = mystr[win_end]
        if right in hashmap:
            hashmap[right] -= 1
            if hashmap[right] == 0:
                matched -= 1
        
        while matched == 0 and (win_end-win_start+1) < maxlen:
            maxlen = min(maxlen, (win_end-win_start+1))
            finstring = mystr[win_start:win_end+1]
        
            if win_end-win_start+1 >= len(pattern):
                left = mystr[win_start]
                if left in hashmap:
                    if hashmap[left] == 0:
                        matched += 1
                    hashmap[left] += 1
                win_start += 1
    return finstring

        




print(smallest_window("aabdec","abc"))
print(smallest_window("abdabca","abc"))
print(smallest_window("adcad","abc"))