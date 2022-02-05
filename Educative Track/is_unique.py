def isunique(mystr):
    a = sorted(set(mystr))
    b = sorted(mystr)
    print(a,b)
    return a == b


print(isunique('aabcde'))