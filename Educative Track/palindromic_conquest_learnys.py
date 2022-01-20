def reverse(mystr):
    print(mystr)
    return mystr[::-1]

def palindrome(mystr):
    if mystr == reverse(mystr):
        return True

    else:
        return False

mystr = 77
while not palindrome(str(mystr)):
    mystr = mystr + int(reverse(str(mystr)))