
import math
def myfun(*l):
    #sotre occurences in hashmap
    hm = {}
    for i in l:
        if i not in hm:
            hm[i] = 1
        else:
            hm[i] += 1
    #sort the elements by the occurence of eleementx
    newl = sorted(hm.items(),key = lambda x: (x[1], x[0]), reverse = True)
    print(newl)
    #store the number mutilplied by the occurences
    a,b = newl[0][0] * newl[0][1] ,newl[1][0] * newl[1][1]
    
    #store the total occurence of elements with max count
    occurences = newl[0][1]+newl[1][1]

    return math.floor((a+b)/occurences)


print(myfun(6,3,8,10,8,100,100,100,50,50,50,8))
