'''
Exercise 10: Write a program to count occurrences of all characters within a string
Given:
str1 = "Apple"
Expected Outcome:
{'A': 1, 'p': 2, 'l': 1, 'e': 1}

'''
def fun(mystr):
    di = dict()
    for i in mystr:
        if i not in di:
            di[i] = 1
        else:
            di[i] = di[i] + 1
    return di


print(fun('Apple'))
