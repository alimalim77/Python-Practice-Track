from enum import Flag


def change(myinp):
    if myinp < 0:
        is_neg = True
    else:
        is_neg = False
    
    mystr = ""
    for i in str(myinp):
        if i.isdigit():
            mystr += i
        
    if is_neg:
        return '-' + mystr
    else:
        return mystr


inp = int(input())
out = change(inp)
print(type(out),out)