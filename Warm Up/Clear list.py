# #Clear list using clear function
# def fun():
#     li = [1,2,3,5]
#     li.clear()
#     print(li)

# fun()

#Clear list using while loop
# def fun():
#     li = [1,2,3,5]
#     while li:
#         del li[0]
# fun()

#Clear list using slicing
def fun():
    li = [1,2,3,5]
    del li[:]
    print(li)
fun()
