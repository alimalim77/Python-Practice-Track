# A = 65
# BB = 66
# CCC
# DDDD
con = 1
inp = int(input())
for i in range(65,65+inp,1):
    for j in range(i,i+con,1):
        print(chr(i),end="")
    con += 1
    print("")