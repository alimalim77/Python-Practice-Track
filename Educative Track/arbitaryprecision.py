#arbitaryprecision

def foo(element):
    total = -(len(element))
    i=-1

    while i >= total:
        if i == -1:
            element[i] = element[i]+1

        if element[i] >= 10:
            sub = element[i]%10
            element[i] = sub
            element[i-1] = element[i-1] + 1
        
        if element[0] == 10:
            element[0]=1
            element.append(0)
        i -= 1
    
    print(element)
    retlist = "".join(map(str,element))
    print(retlist)


naam = [9,9,8]
foo(naam)