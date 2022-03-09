s = set()
def isHappy(n):
    if n == 1:
        return True
    li = list(map(int,str(n)))
    sqli = [x*x for x in li]
    b = sum(sqli)
    if b in s:
        return False
    else:
        s.add(b)
        return isHappy(b)

print(isHappy(7))