inp = int(input())
li = []
def backtrack(n,*words):
    a,b = words
    for i in range(n):
        if len(li) == 9:
            return

        for i in (a,b):
            if i-1 >= 0 and i+1 <= len(li):
                li[i-1] != a and li[i+1] != a:
                li.append(i)
        li.pop()
backtrack(inp,'X','Y')

