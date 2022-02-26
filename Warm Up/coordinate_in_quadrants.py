#(x,y)
cx = int(input("Enter x coordinate"))
cy = int(input("Enter y coordinate"))

if cx > 0 and cy > 0:
    cor = 1
elif cx < 0 and cy > 0:
    cor = 2
elif cx < 0 and cy < 0:
    cor = 3
elif cx > 0 and cy < 0:
    cor = 4
else:
    cor = 0
print("The coordinate is", cor)