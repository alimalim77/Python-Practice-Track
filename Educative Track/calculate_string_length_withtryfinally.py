
from typing import final

def fun(mystr,i = 0):
    e = False
    try:
        print(mystr[i])
    except:
        if IndexError:
            e = True
    finally:
        if e:
            return i
        return fun(mystr,i+1)
    #print(i)
    

print(fun("kanyeWest"))
