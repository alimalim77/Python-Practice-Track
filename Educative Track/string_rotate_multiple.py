'''
There are a number of space separated strings. Each string is in the form of, alphabet:number. From each string extract the number and rotate the string rightwards if the number is even or leftwards if the number is odd. The rotation should be by as many places as the extracted number.
If input is not valid print -1.

Input format:
Space separated strings in a single line.

Output format:
Multiple lines of output, each line having a single string.

Sample input: 
hello:11 card:26

Sample output: 
elloh
rdca

'''
def leftrotate(name,number):
    rot = int(number) % len(name)
    return name[rot:]+name[:rot]
    
    

def rightrotate(name,number):
    rot = int(number) % len(name)
    return name[rot:]+ name[:rot]

inp = input("Enter the choice")

s1 = list(map(str,inp.split()))
s2= []
for i in s1:
    s2.append(tuple(map(str,i.split(":"))))

print(s2)
for i in s2:
    if len(i)%2 == 0:
        print(rightrotate(i[0],i[1]))
    else:
        print(leftrotate(i[0],i[1]))