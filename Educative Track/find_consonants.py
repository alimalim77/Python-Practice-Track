vowels = ['a','e','i','o','u']
ctr = 0
def fun(mystr,i = 0,grt=0):
    if mystr == "":
        return grt
    if mystr[0] in vowels:
        grt += 1
        return fun(mystr[1:], i+1,grt)
    return fun(mystr[1:],i+1,grt)


print(fun("kanyeWest"))