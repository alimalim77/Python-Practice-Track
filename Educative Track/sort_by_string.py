def fun(s):
    res = s.split(" ")
    ans = []
    for word in res:
        string,val = [],None
        for i in word:
            
            if i.isdigit():
                val = int(i)
            else:
                string.append(i)
        string = "".join(string)
        ans.append((string,val))
    ans.sort(key = lambda x:x[1])
    retstr = []
    for i in ans:
        retstr.append(i[0])
    return " ".join(retstr)


print(fun("is2 Thi1s T4est 3a"))