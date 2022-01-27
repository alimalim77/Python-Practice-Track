'''
Exercise 4: Arrange string characters such that lowercase letters should come first
Given string contains a combination of the lower and upper case letters. 
Write a program to arrange the characters of a string so that all lowercase letters should come first.

Given:
str1 = PyNaTive
Expected Output:
yaivePNT

'''
def fun(str1):
    list1 = []
    list2 = list()

    listcheck = list(str1)

    for i in listcheck:
        if i.isupper():
            list1.append(i)
        else:
            list2.append(i)
    
    list2.extend(list1)
    return "".join(list2)

print(fun('PyNaTive'))