
def fun(mystr,i = 0):
    if i >= len(mystr):
        return "Not present"
    if mystr[i].isupper():
        return str(i) + " is uppercase"
    else: 
        return fun(mystr,i+1)

print(fun("kanyeWest"))