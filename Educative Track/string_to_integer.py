def str_to_int(mystr):
    if mystr[0] == '-':
        mystr = mystr[1:]
        is_neg = True
    else:
        is_neg = False
    
    inp = 0
    
    i = 0
    while i < len(mystr):
        inp = inp * 10 + (ord(mystr[i]) - ord('0'))
        i += 1
    if is_neg:
        return inp * -1
    else:
        return inp


print(str_to_int('-121'))