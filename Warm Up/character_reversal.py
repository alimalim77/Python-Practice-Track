'''
Character Reversal
D
CD
BCD
ABCD
'''

def pattern(n):
    a = (ord('A')+n-1)

    for i in range(1,n+1,1):
        for j in range(0,i,1):
            print(chr(a+j),end= "")
        a = (ord('A')+n-1)-i
        print()

pattern(int(input("Enter the number")))