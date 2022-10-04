res = []
index = [0]
def comsum(li,count,target):
    totsum = sum(count)
    if totsum >=  target:
        if totsum == target:
            res.append(count[:])
        return 
    #print(dic
  
    for num in range(len(li)):
        if num < index[0]:
            continue
        count.append(li[num])
        comsum(li,count,target)
        count.pop()
    index[0] += 1


print(comsum([2,3,6,7],[],7))
print(res)