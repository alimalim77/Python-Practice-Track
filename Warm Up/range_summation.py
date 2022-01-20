#summantion of a given range
start = int(input("Enter the input for starting range"))
end = int(input("Enter the inpur for end range"))

ctr = 0
for i in range(start,end+1):
    ctr = ctr + i

print(ctr)