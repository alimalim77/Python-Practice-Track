#Condition 1 : Check if three is present in the number 
def checker(num):
    if '3' in num:
        return True
    else:
        return False

#Check if the preceeding degits are lesser than the current digit
def passer(n):
    totlen = len(n)
    count =  0 
    for i in range(1,totlen):
        count += int(n[i-1])
        if count >= int(n[i]):
            return True
    return False


#Main 
u = int(input())
l = int(input())
d = int(input())

for i in range(l,u+1):
    if checker(str(i)) or passer(str(i)[::-1]):
        continue
    print(i)


    

