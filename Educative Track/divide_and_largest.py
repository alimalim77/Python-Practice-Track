def fun(first,second,thrid):
    mat = []
    hm = {}
    column = 1
    for i in range(0,first-1,third):
        mat.append(second[i:i+third])
        if len(mat[-1])==third:
            hm[column] = sum(mat[-1])
        #print(mat,hm)
        column += 1
    n = sorted(hm.items(),key = lambda x: (-x[1],x[0]))
    return n[0][0]+1
    



first = 12 #int(input())
second = [14,9,19,6,13,13,3,2,12]#list(map(int,input().split()))
third = 3 #int(input())
print(fun(first,second,third))