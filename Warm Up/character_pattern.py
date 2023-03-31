'''
Character Pattern
A
BC
DEF
GHIJ
'''

def pattern(n):
    a = 65

    for i in range(1,n+1,1):
        for j in range(0,i,1):
            print(chr(a+j),end="")
        a += (j+1)
        print()
    
    

pattern(int(input("Enter the number")))