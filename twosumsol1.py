def fun(a,tar):
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]+a[j] == target:
                return True
            #print(i,j,end="\n")
    return False




arr = [-2,1,2,4,7,11]
target = 23

print(fun(arr,target))

#complexity of o(n^2)