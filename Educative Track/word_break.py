
def wordBreak(s, words):
    l=[False]*len(s) 
    for i in  range(len(s)) :
        for word in words:
            if i>=len(word)-1 and  ( i==len(word)-1  or l[i-len(word)]  ) :
              if word==s[i-len(word) +1:i+1]:
                l[i] =True 
                break
    return l[-1]
print(wordBreak("catsanddogs",["cats","and","ogs"]))