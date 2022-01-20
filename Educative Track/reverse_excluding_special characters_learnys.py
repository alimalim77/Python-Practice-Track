'''You are given a string consisting of alphabets, digits and special characters. You are asked to reverse the string while maintaining
 the location of all the special characters. The input string is guaranteed to have at-least one character. 

Input format:
Single line of alphanumeric string.

Output format:
Single line of alphanumeric string.

Sample input:
sd&hg#j

Sample output:
jg&hd#s
'''
li = []

mystr = input("Enter a string")
inili = list(mystr)
ctr = 0
for i in mystr:
    if (ord(i) >= ord('A') and ord(i) <= ord('Z')) or (ord(i) >= ord('a') and ord(i) <= ord('z')) or (ord(i) >= ord('1') and ord(i) <= ord('9')):
        li.append((i,ctr))
    ctr += 1


newstr = ""
for i in range(len(li)):
    newstr = newstr + li[i][0]
revli  = list(newstr)

ctr=0
for i in mystr:
     if (ord(i) >= ord('A') and ord(i) <= ord('Z')) or (ord(i) >= ord('a') and ord(i) <= ord('z')) or (ord(i) >= ord('1') and ord(i) <= ord('9')):
        inili[ctr] = revli.pop()
     ctr += 1    
newstr = "".join(inili)
print(newstr)

