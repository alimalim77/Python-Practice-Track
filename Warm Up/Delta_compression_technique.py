inputList = list(map(int,input().split()))
finalList = []
cur = 0
for i in inputList:
    ad = i+cur
    finalList.append(ad)
    cur = ad
print(finalList)