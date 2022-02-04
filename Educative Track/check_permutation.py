def checkstring(mystr1, mystr2):
    '''
    using normal sorting and assigning gives a time complexity of O(nlogn) with no extra space thus a 
    space complexity of O(1) is obtained.
    However, using hastable will reach a time complexity of O(n) with a hashtable increaing the 
    space complexity
    '''
    if len(mystr1) != len(mystr2):
        return False
    di = dict()
    for i in mystr1:
        if i not in di:
            di[i] = 0
        else:
            di[i] += 1

    for i in mystr2:
        if i in di:
            di[i] -= 1
        else:
            continue
        if di[i] < 0:
            di.pop(i)
    print(di)
    if di == {}:
        return True
    else:
        return False        


print(checkstring("googel","googef"))