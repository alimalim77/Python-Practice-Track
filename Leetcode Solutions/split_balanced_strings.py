def balancedStringSplit(s):
        count = 0
        ctr = 0
        for i in s:
            if i == "R":
                ctr += 1
            elif i == "L":
                ctr -= 1
            if ctr == 0:
                count += 1
        return count

            
        
#print(balancedStringSplit("RLRRLLRLRL"))
#print(balancedStringSplit("RLLLLRRRLR"))
#print(balancedStringSplit("LLLLRRRR"))
print(balancedStringSplit("RLRRRLLRLL"))

                
                