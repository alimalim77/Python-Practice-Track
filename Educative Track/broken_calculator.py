from tracemalloc import start


def check(num,fin):
    if num < fin and fin%num == 0:
        return True
    


def brokenCalc(startValue, target):
    '''
    ctr = 0
    while startValue != target:
        print(startValue,target)
        if check(startValue, target):
            startValue *= 2
        elif startValue < target and  (target-1% (startValue)) == 0:
            print(target%(startValue))
            startValue -= 1
        #elif startValue < target and (startValue * 2)  
        elif startValue < target:
            startValue *= 2
        else:
            startValue -= 1
        ctr += 1
    return ctr
    '''
    ctr = 0
    while target > startValue:
        if target % 2 == 1:
            target = target  + 1
        elif target % 2 == 0:
            target //= 2
        ctr += 1
    return ctr + (startValue-target)
print(brokenCalc(3,2))