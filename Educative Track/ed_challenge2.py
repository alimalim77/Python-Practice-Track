def foobar(mystr, pattern):
    pattern = sorted(pattern) 
    par = len(pattern)
    for i in range(0,len(mystr),1):
        print(sorted(mystr[i:i+par]))
        if sorted(mystr[i:i+par]) == pattern:
            li = []
            for j in range(i,i+par):
                li.append(j)
            return li
    return []
        
print(foobar("ppqp","pq"))