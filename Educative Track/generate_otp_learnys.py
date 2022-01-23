'''
Generate a 4 digit OTP from a given number. 
The process to generate the OTP is as follows. 
Starting from the first position, generate a 4 digit OTP by concatenating the squares of these digits..    

Input Format:
An integer number.

Output Format:
A 4 digit integer number.

Sample Input
4365188

Sample Output
1693

'''


def genotp(mystr):
    otp = ""
    for i  in mystr:
        if len(otp) >= 4:
            otp = otp[:4]
            return int(otp)
        otp = otp + str((int(i) **2))
    

inp = int(input())
final =  genotp(str(inp))
print(final)
