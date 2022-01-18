#Determine if brackets are balanced
'''
[{()}] 
'''

from stack import Stack


def is_match(top, para):
    if top == '[' and para == ']':
        return True
    if top == '{' and para == '}':
        return True
    if top == '(' and para == ')':
        return True
    else:
        return False

def isbal(thestring):
    s = Stack()
    balanced = True
    index = 0
    lengthstr = len(thestring)

    while index < lengthstr and balanced:
        para = thestring[index]
        if para == ('[' or '{' or '('):
            s.push(para)
        else: 
            if s.is_empty():
                balanced = False
                break

            else:
                top = s.pop()
                if not is_match(top, para):
                    balanced = False
                    break
        index += 1
 
    if s.is_empty() and balanced:
        print("Balanced")
    else:
        print("Not Balanced")

    

isbal("[[]]}")
    