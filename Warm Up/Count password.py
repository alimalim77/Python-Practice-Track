#Take the input and split them
#Count for occurence of char in password
# Check if occurence is between the the range

def fun(mystr):
    rng, char, password = mystr.split(" ") # 3-6 stored in rng, 3 stored in char and allstars stored in pass
    minrange,maxrange = map(int,rng.split("-")) # 3 and 6 assigned
    

    count = password.count(char)
    # for i in password:
    #     if char == i:
    #         count += 1
    
    #Final COndition
    if minrange <= count <= maxrange:
        print("Valid Password")
    else:
        print("Not Valid")
    


fun("3-6 a allstars")
