def fun(mystr):
    rng, char, password = mystr.split(" ") # 3-6 stored in rng, 3 stored in char and allstars stored in pass
    minrange,maxrange = map(int,rng.split("-")) # 3 and 6 assigned
    
    if password[minrange-1]==char and password[maxrange-1]==char:
        print("Not Valid")
    elif password[minrange-1]==char or password[maxrange-1]==char:
        print("Valid")
    else:
        print("Not Valid")
    
    
    


fun("3-6 a allstars")
