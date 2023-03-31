import numpy as np
from functools import reduce
from operator import mul
# Using Multiplcation
# def multiply():
#     li = [2,4,6,8]
#     ans = 1
#     for i in li:
#         ans *= i
#     return ans
#multiply()


#Using Numpy
# def fun():
#     li = [2,4,6,8]
#     ans = np.product(li)
#     print(ans)
# fun()

#Using Reduce + Mul 
# def fun():
#     li = [2,4,6,8]
#     ans = reduce(mul,li)
#     print(ans)
# fun()

#Using Product
def fun():
    li = [2,4,6,8]
    ans = reduce(mul,li)
    print(ans)
fun()