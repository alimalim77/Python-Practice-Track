#buy sell stock
li = [310,315,275,295,260,270,290,230,255,250]


tupmax = tuple((li[0],0))
tupmin = tuple((li[0],0))
ctr= li[0]
profit_daily = []

for i in range(0,len(li)):
    for j in range(i+1,len(li)-1):
        if li[j+1] - li[i+1] > li[j]-li[i]:
            profit = li[j+1] - li[i+1]
            profit_daily.append(profit)


print(max(profit_daily))
    

