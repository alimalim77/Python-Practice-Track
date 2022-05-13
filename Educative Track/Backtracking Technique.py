def bct(n,li = []): 
    print(li)
    if len(li) >= n:
        return
    for i in range(n):
        li.append(i)
        bct(n,li)
        li.pop()

print(bct(4))