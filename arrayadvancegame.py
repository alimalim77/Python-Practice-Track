#greedy approach

def foo(rec):
    ctr = len(rec)
    i = 0
    curin = rec[i]
    while i < ctr:
        if i >= ctr-1:
            print("possible")
            break
        
        if curin != 0:
            curin = rec[i]
            i = i + curin
        else:
            print("not possible")
            break


name = [1,2,0,0,2,0,1]
foo(name)