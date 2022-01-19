#buy sell stock
prices = [310,315,275,295,260,270,290,230,255,250]

profit_daily = []

for i in range(0,len(prices)):
    for j in range(i+1,len(prices)-1):
        if prices[j+1] - prices[i+1] > prices[j]-prices[i]:
            profit = prices[j+1] - prices[i+1]
            profit_daily.append(profit)


print(max(profit_daily))
    

