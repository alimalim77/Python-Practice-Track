#buy sell stock solution 2
prices= [310,315,275,295,260,270,290,230,255,250]

profit = 0.0
minprice = float('inf')
maxprofit = 0

for price in prices:
    minprice = min(minprice,price)
    profit = price - minprice
    maxprofit = max(profit,maxprofit) 


print(maxprofit)