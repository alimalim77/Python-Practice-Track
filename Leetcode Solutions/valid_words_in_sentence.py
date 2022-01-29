def inc(mystr):
    a = mystr.count('.') + mystr.count(',') + mystr.count('!')
    if a == 1:
        if mystr[-1] in [',','.','!']:
            return 1
        else:
            return 0
    if a == 0:
        return 1

def fun(sentence):
    sentence = sentence.split()
    r,m = 0,0
    
    di = list(map(str,[0,1,2,3,4,5,6,7,8,9]))

    li = []
    for s in sentence:
        flag = 0
        for j in s:
            if j in di:
                flag=1
        if flag == 0:
            li.append(s)
    print(li)        
    su = 0 
    for i in li:
        m = i.count('-')
        if m == 1:
            a = i.index('-') 
            if a != 0 and a != len(i)-1 and i[a+1].isalpha():
                r = inc(i)
                su = su + r
        elif m==0:
            r = inc(i)
            su = su + r
    return su

print(fun('Hel3lo Wor3ld Time to hhf gfh-g'))
