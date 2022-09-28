# "oidbcaf" and "abc"
# Permutation in abc, acb, bac, bca, cab, cba
def string_anagrams(mystr,pattern):
    matched, win_start = 0,0
    hashmap = {}
    res = []

    for char in pattern:
        if char not in hashmap:
            hashmap[char] = 0
        hashmap[char] += 1

    for win_end in range(len(mystr)):
        right = mystr[win_end]
        if right in hashmap:
            hashmap[right] -= 1
            if hashmap[right] == 0:
                matched += 1
        
        if matched == len(hashmap): #3 and #3
            res.append(win_start)

        if win_end >= len(pattern)-1:
            left = mystr[win_start]
            win_start += 1

            if left in hashmap:
                if hashmap[left] == 0:
                    matched -= 1
                hashmap[left] += 1
    return res

print(string_anagrams("ppqp","pq"))
print(string_anagrams("abbcabc","abc"))