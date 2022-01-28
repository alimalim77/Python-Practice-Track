'''
Exercise 11: Reverse a given string
Given:
str1 = "PYnative"
Expected Output:
evitanYP

'''

from copy import deepcopy


def fun(mystr):
    #revstr = list(mystr)
    #newstr = deepcopy(revstr)
    #print(newstr)
    #newstr.reverse()
    #return newstr
    return mystr[::-1]

print(fun('Apple'))
