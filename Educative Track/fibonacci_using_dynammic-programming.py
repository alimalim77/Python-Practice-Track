con ={}

def fib(n):
    print(con)
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n in con:
        return con[n]
    else:
        con[n] =  fib(n-1) + fib(n-2)
    return con[n]
        #if n in con:
            #return con[n]
print(fib(7))