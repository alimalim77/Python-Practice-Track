'''
Alpha Pattern
A = 1
BB = 2
CCC = 3
'''

def pattern(n):
    count  = 1

    for i in range(65,65+n,1):
        for j in range(i,i + count,1):
            print(chr(i),end="")
        count += 1
        print()
    
pattern(int(input("Enter the number")))