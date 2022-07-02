from pyparsing import Word

visited = set()
def bct(n,check,visited,li = []): 
    if len(li) >= 3:
        if "".join(li) not in visited and len(set(li)) == check:
            visited.add("".join(li))
        return
    for i in n:
        li.append(i)
        bct(n,check,visited,li)
        li.pop()
newstr = "llo"
bct(newstr,len(set(newstr)),visited)
print(visited)