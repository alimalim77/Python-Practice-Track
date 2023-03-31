dic = {
    "2":'abc',
    "3":'def', 
    "4":'ghi',
    "5": 'jkl',
    "6":'mno',
    "7":'pqrs',
    "8":'tuv',
    "9":'wxyz'
}
res = []
def lettercombinations(num,word,count):
    if count ==  0:
        res.append("".join(word))
        print(res)
        return 
    #print(dic)
    s = dic[num[0]]
    for char in s:
        word.append(char)
        lettercombinations(num[1:],word,count-1)
        word.pop()




print(lettercombinations("23",[],2))
print(res)