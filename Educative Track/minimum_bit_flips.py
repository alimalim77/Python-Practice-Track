def minBitFlips(start, goal):
    a= bin(start)
    b = bin(goal)
    a,b = a[2:],b[2:]
    l = max(len(a),len(b))
    mi = a if len(a) < len(b) else b
    
    if a==mi: ma = b
    else: ma = a
    
    while l != len(mi):
        mi = '0' + mi
    print(ma,mi)
    ctr = 0
    for i in range(len(ma)-1,-1,-1):
        if ma[i] != mi[i]:
            ctr+=1
        
    return ctr

print(minBitFlips(7,10))