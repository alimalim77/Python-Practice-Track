def integer_square_root(k):
    i = 0
    j = k

    while i <= j:
        mid = (i+j)//2
        midsq = mid * mid

        if midsq <= k:
            i = mid+1
        else:
            j = mid-1
    return i-1
   
 
   
k = 300
print(integer_square_root(1))
