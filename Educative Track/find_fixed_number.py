from xml.dom import minidom


def fixedpoint(num):
    i = 0
    j = len(num)-1
    mid = (i+j)//2

    while i <= j:
        if num[mid] == mid:
            return True
        if num[mid] < mid:
            i = mid + 1
            mid = (i+j)//2
        if num[mid] > mid:
            j = mid-1
            mid = (i+j)//2
    return False


print(fixedpoint([2,7,3,13,8,9,24]))