'''
Given a string consisting of digits and alphabets. 
Extract the digits from the string and form a number and print it.

Input Format:
Single line of string.

Output Format:
An integer.

Sample Input: 
a3h0uy48==8$uss1 nj29

Sample Output: 
30488129
'''
inp = input()
newlist = []

for i in inp:
    if i.isdigit():
        newlist.append(i)
finalstr = "".join(newlist)
print(finalstr)