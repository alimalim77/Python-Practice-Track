#timecomplexity of O(n) and space O(1)

def fun(a,tar):
    i=0
    j=len(a)-1

    while i<j:
        if a[i]+a[j] == target:
            print(a[i],a[j])
            return True
        elif a[i]+a[j] < target:
            i=i+1
        else:
            j=j-1
    return False

arr = [-2,1,2,4,7,11]
target = 13

print(fun(arr,target))