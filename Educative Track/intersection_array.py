#intersection_program without builtin function
a = [2,7,45,8,54,3,7,9]
b = [4,6,7,3,8,4,3]
a.sort()
b.sort()

i=0
j=0
c = []


while i<len(a) and j<len(b):
    if a[i] < b[j]:
        i = i + 1
    elif a[i] > b[j]:
        j = j + 1
    elif a[i]==b[j] and b[j] != b[j-1]:
        c.append(b[j])
        i = i+1 
        j = j+1
    else:
        i = i+1 
        j = j+1
print(c)


