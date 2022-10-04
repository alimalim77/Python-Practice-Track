def partition(s):
    res = []
    part = []
        
    def backtrack(i):
        if i <= 0:
            res.append(part[:])
            return
        for j in range(0,i,1):
            word = s[j:i]
            if word == word[::-1]:
                part.append(word)
                backtrack(j-1)
                part.pop()
    backtrack(len(s))
    return res
print(partition("aab"))