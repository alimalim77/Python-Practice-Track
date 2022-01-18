# use of break and continue
#add all numbers until 20, move if 13 comes in between

for i in range(0,20):
    if i == 13:
        break
    print(i)

for i in range(0,20):
    if i == 13:
        continue
    print(i)
