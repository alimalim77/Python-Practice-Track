'''
Exercise 7: String characters balance Test
Write a program to check if two strings are balanced. 
For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2.
 The character’s position doesn’t matter.
Given:
Case 1:
s1 = "Yn"
s2 = "PYnative"
Expected Output:
True
Case 2:
s1 = "Ynf"
s2 = "PYnative"
Expected Output:
False

'''
def fun(s1 ,s2 ):

    flag = 1    
    for i in range(len(s1)):
        if s1[i] not in s2:
            flag = 0

    if flag == 1:
        return True
    else:
        return False

print(fun(input("Enter first input"),input('Enter second input')))