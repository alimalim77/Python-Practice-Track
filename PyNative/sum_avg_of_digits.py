'''
Exercise 9: Calculate the sum and average of the digits present in a string
Given a string s1, write a program to return the sum and average of the digits 
that appear in the string, ignoring all other characters.

Given:
str1 = "PYnative29@#8496"
Expected Outcome:
Sum is: 38 Average is  6.333333333333333

'''
def fun(mystr):
    li = list()

    for i in mystr:
        if i.isdigit():
            li.append(i)
        
    sum = 0
    for i in li:
        sum = sum + int(i) #typecasting to avoid string arithmetic error
    avg = sum/len(li)
    return sum,avg


print(fun('PYnative29@#8496'))