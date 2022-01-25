'''
Given a set of strings. Each string consists of small case alphabets. 
Sort each string in the increasing order of the frequency of characters.
 If the frequency of two characters is the same,
  the character coming EARLIER in lexicographical order should come first.

Input format:
Multiple strings in a single line separated by space.

Output format:
Multiple strings in a single line separated by space.

Sample input:
abbaccde bdettytbe

Sample output:
deaabbcc dybbeettt

'''



def ischeck(mystr):
    dicstore = dict()
    for i in mystr:
        if i not in dicstore:
            dicstore[i] = 1
        else:
            dicstore[i] += 1
    newd = sorted(dicstore.items(), key= lambda x : (x[1],x[0]))
    
    retstr= ""
    for i in newd:
        retstr += i[0]*i[1]
    print(retstr, end=" ")
    




inp = input().split()
for i in inp:
    ischeck(i)