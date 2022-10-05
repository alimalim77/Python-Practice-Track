
def klengthwords(string,k,count,s):
    if k==0:
     
        count += 1
        return count
    for i in range(len(string)):
        if i in s:
            continue
        s.add(i)
        count = klengthwords(string,k-1,count,s)
        s.remove(i)
    return count



k = 3
print(klengthwords("geeksforgeeks",k,0,set()))