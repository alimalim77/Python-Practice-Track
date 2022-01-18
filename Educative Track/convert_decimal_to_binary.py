''' Problem: Decimal To Binary'''

from stack import Stack

def convert_int_to_bin(decimal):
    
    if decimal == 0:
        return 0

    s = Stack()

    while decimal > 0:
        remainder = decimal % 2
        s.push(remainder)
        decimal = decimal //2


    store = ""
    while not s.is_empty():
        store += str(s.pop())

    return store



stringfound = convert_int_to_bin(565)
print(stringfound)




'''num =123(1),61(1),30(0),15(1),7(1),3(1),2(0)
 |  |
 |  |
 |  |
 |  |
'''