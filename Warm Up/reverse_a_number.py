#reverse a number
from asyncio.windows_events import NULL


myinp = int(input("Enter a number"))
rev = 0

while myinp != 0:
    rev = rev*10
    rem = myinp % 10
    rev = rev + rem
    myinp = myinp//10
print(rev)


'''
12343
ext 3
rev = 3*10
ext 4
rev = (30 + 4)* 10
340
ext  3
3430
ext 2
34320
ext
34321 

'''