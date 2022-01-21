'''
Given a string consisting of digits, alphabets and special characters. 
Modify the string by sorting the digits (increasing order) and print the modified string. 

Input Format:
An alphanumeric string in a single line. 

Output Format:
An alphanumeric string in a single line. 

Sample Input: 
a2b4c60d4

Sample Output: 
a0b2c44d6
'''
inp = input()
linum = list()

for i in inp:
    if i.isdigit():
        linum.append(i)
linum.sort()

inp1  = []
for i in inp:
    inp1.append(i)

for i in range(len(inp1)):
    if (ord(inp[i]) >= ord('0') and ord(inp[i]) <= ord('9')) and linum:
        a = linum.pop(0)
        inp1[i] = a
print("".join(inp1))
