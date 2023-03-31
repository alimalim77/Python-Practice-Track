'''
   1
  12
 123
1234
'''

def pattern(n):
    shift = n-1
    for i in range(n):
        top = 1
        for j in range(n):
            if j >= shift:
                print(top,end="")
                top += 1
            else:
                print(" ",end="")
        print()
        shift -= 1

pattern(int(input("Enter the number")))