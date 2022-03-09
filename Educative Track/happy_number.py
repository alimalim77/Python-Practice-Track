s = set()
def isHappy(n):
    li = list(map(int,str(n)))
    sqli = [x*x for x in li]
    b = sum(sqli)
    if b in s:
        return False
    if b == 1:
        return True
    
    else:
        s.add(b)
        return isHappy(b)

print(isHappy(2))