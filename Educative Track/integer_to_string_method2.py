def change(myinp):
    if myinp < 0:
        is_neg = True
        myinp *= -1
    else:
        is_neg = False
    
    mystr = []
    if myinp == '0':
        mystr.append('0')
    else:
        while myinp > 0:
            mystr.append(chr(ord('0') + myinp%10))
            myinp = myinp // 10
        mystr = mystr[::-1]
    mystr = "".join(mystr)
    if is_neg:
        return '-' + mystr
    else:
        return mystr


inp = int(input())
out = change(inp)
print(type(out),out)