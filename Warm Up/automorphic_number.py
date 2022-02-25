inp = int(input("Enter the number"))

oldvar = inp
storedi = 0
square = inp * inp

while inp != 0:
    inp = inp // 10
    storedi += 1

newvar = 0
while storedi != 0:
    rem = square % 10
    newvar = newvar * 10 + rem
    square //= 10
    storedi -= 1

if oldvar == newvar:
    print('Automorphic')