from pyparsing import Word


def bct(n,li = []): 
    print(li)
    if len(li) >= 3:
        return
    for i in Word:
        li.append(i)
        bct(n,li)
        li.pop()

print(bct())