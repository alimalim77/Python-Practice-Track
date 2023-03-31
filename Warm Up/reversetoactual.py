def numpop(n):
    count=0
    for num in reversed(n):
    
         count *= 10
         count += num
    
    rev = int(str(count)[::-1])
    

    
    # secsum = 0
    # for num in n:
    #     secsum *= 10
    #     secsum += num

    return count,rev

def backtrack(num,count,bar):
    a,b = numpop(count)
    if num == (a+b):
        print(a,b)
        return True
    if len(count) == bar:
        return False
    for i in range(10):
        count.append(i)
        ans = backtrack(num,count,bar)
        if ans: return True
        count.pop()
    return False



bre = list(str(181))
print(backtrack(181,[],len(bre)))

