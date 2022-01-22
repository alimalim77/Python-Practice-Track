'''
Given a set of strings. Remove all the consecutive duplicate characters from each string and print the set.

Input format:
Multiple strings in a single line separated by space. 

Output format:
Multiple strings in a single line separated by space. 

Sample Input
ppaarroott eeaaggllee
Sample Output
parot eagle
'''
strlist = list(map(str,input().split()))
newlist = []

for i in strlist:
    a = i
    j=0
    while j < len(a)-1:
        if a[j+1] == a[j]:
            a = a[0:j+1] + a[j+2:]
        j = j+1
    newlist.append(a)

for i in newlist:
    print(i,end=" ")