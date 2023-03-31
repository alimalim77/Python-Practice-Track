from turtle import right


def word_concat(target, strlist):
    res = []

    wordmap = {}
    for word in strlist:
        if word not in wordmap:
            wordmap[word] = 0
        wordmap[word] += 1
    
    for i in range(0,len(target)- (len(strlist)*len(strlist[0]))+1):
        word_seen = {}
        win_start = i
        matched, flag  = 0, False
        for win_end in range(i,i+((len(strlist)*len(strlist[0])))):
            if win_end - win_start + 1 == len(strlist[0]) and target[win_start:win_end+1] in wordmap:
                flag = True
                #matched += 1
                val = target[win_start:win_end+1]
                if val not in word_seen:
                    word_seen[val] = 0
                word_seen[val] += 1
            
            if win_end - win_start + 1 == len(strlist[0]):
                win_start += 1
            if word_seen == wordmap and flag:
                res.append(i)
    
                break  

    return res





print(word_concat("catfoxcat",["cat","fox"])) # [0,3]
print(word_concat("catcatfoxfox",["cat","fox"])) # [3]

