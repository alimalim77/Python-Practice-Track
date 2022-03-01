def binsearch(*nums):
    li = list(map(int,nums))
    i = 0 
    j =len(li)-1
    def binsea(i,j,target,li):
        if i > j:
            return False
        mid = (i + j)//2
        if target == li[mid]:
            return True
        if li[mid] > target:
            return binsea(i,mid-1,target,li)
        if li[mid] < target:
            return binsea(mid+1,j,target,li)
    a = binsea(i,j,16,li)
    if a:
        print(True)
    else:
        print(False)

binsearch(3,6,8,9,16,19,26,78)