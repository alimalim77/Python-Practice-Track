'''
Exercise 5: Count all letters, digits, and special symbols from a given string
Given:
str1 = "P@#yn26at^&i5ve"
Expected Outcome:
Total counts of chars, digits, and symbols 
 
Chars = 8 
Digits = 3 
Symbol = 4
'''
def fun(str1):
    Chars =  0
    Digits =  0
    Symbol = 0
    
    for i in str1:
        if i.isdigit():
            Digits = Digits +1
        elif i.isalpha():
            Chars = Chars + 1
        else:
            Symbol = Symbol + 1
    print(Chars,type(Chars),end= "\n")
    print(Digits,type(Digits),end= "\n")
    print(Symbol)
    
    

fun('Farukh259')
