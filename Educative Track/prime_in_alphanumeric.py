'''
From a given alphanumeric string extract all the digits,
remove duplicate digits (remove the later appearances of the digit) and from this set of digits construct a number.
The digits in the formed number should maintain their positions relative to each other. 
Finally, check whether the number thus formed is prime or not.

Input Format:
An alphanumeric string in a single line.

Output Format:
True if the formed number is prime False otherwise.

Sample Input: 
a2b4c6d4

Sample Output: 
False

'''
def checkprime(mystr):
    numcheck = int(mystr)
    for i in range(2,numcheck):
        if numcheck % i == 0:
            return False
    return True
    
mystr1 = input()
numstr = ""
for i in mystr1:
    if i.isdigit() and i not in numstr:
        numstr = numstr + i

print(checkprime(numstr))

