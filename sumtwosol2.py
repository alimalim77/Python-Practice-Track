def fun(a,tar):
    ht = dict()
    for i in range(len(a)):
        if a[i] in ht:
            print(ht[a[i]],a[i])
        else:
            ht[target - a[i]] = a[i]


arr = [-2,1,2,4,7,11]
target = 13

#o(n complexity time and space both)