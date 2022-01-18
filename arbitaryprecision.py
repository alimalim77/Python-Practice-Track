#arbitaryprecision

def foo(naam):
    total = -(len(naam))
    i=-1

    while i >= total:
        if i == -1:
            naam[i] = naam[i]+1

        if naam[i] >= 10:
            sub = naam[i]%10
            naam[i] = sub
            naam[i-1] = naam[i-1] + 1
        
        if naam[0] == 10:
            naam[0]=1
            naam.append(0)
        i -= 1
    
    print(naam)
    retlist = "".join(map(str,naam))
    print(retlist)


naam = [9,9,8]
foo(naam)