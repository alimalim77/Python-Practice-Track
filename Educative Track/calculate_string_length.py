def fun(mystr):
    if mystr == "":
        return 0
    return 1 + fun(mystr[1:])
    

print(fun("kanyeWest"))
