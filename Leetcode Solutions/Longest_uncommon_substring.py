def lengthOfLongestSubstring(s):
        if s == " ":
            return 1
        if s == "":
            return 0
        ht = {}
        maxctr = 0
        for i in s:
            if len(ht) > maxctr:
                maxctr = len(ht)
            if i not in ht:
                ht[i] = 1
            else:
                
                ht.clear()
                ht[i] = 1 
        if len(ht) > maxctr:
            maxctr = len(ht)
        print(maxctr)

lengthOfLongestSubstring('dvdf')