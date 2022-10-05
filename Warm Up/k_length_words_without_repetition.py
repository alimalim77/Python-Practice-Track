s =set()
def klengthwords(n,k,count):
    if k==0:
        count += 1
        return count
    
    for i in range(n):
        if i in s:
            continue
        s.add(i)
        count = klengthwords(n,k-1,count)
        s.remove(i)
    return count

k = 3
string = "geeksforgeeks"
n= len(string)
print(klengthwords(n,k,0))
# s =set()
# def klengthwords(n,k,count):
#     if k==0:
#         count += 1
#         return count
    
#     for i in range(n):
#         if i in s:
#             continue
#         s.add(i)
#         count = klengthwords(n,k-1,count)
#         s.remove(i)
#     return count

# k = 3
# s = "geeksforgeeks"
# print(klengthwords(len(s),k,0))