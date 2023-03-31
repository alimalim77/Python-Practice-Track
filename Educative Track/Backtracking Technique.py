from pyparsing import Word


def bct(n,li): 
    print(li)
    if len(li) >= n:
        return
    if li and li[-1] == 'X':
        flag = False
    else:
        flag = True
    for i in range(n):
        li.append(li[0]) if flag else li.append(li[1])
        bct(n,li)
        li.pop()

print(bct(5,['X','Y']))