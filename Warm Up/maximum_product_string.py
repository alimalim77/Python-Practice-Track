#Py

def maxProduct(words):
    s = set()
    retList = []
    words.sort(key = lambda x: len(x),reverse = True)
    for i in words:
        if len(retList) == 2:
            return len(retList[0])*len(retList[1])
        if len(set(i).intersection(s)) == 0:
            retList.append(i)
            a = [str(b) for b in i]
            for i in a:
                s.add(i)
            print(s)


print(maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))


#Lambda sort using using the length
# CHeck for max two and return if obtained
#Check set by set on what is the prefered string to add
# Occurences 0 will decide and list is already in descending