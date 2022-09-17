#Not Considering stars
def fun():
    for i in range(6):
        for j in range(6):
            #or ((i==6//2) and ((1)<j<3))
            if (((0<i<5)  and (j==0))) or (((i==0 or i ==5) and (0<j<4))) or ((j==5) and (((6//2)<=i<5)) or (i==(6//2)) and ((6//2)<=j<5)):
                print("* ",end="")
            else:
                print(" ",end="")
        print()
            

fun()