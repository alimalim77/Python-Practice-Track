def maxScoreIndices(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lnum = list()
        rnum = list()
        scores = {}
        r,l = 0,0
        for i in range(len(nums)+1):
            lnum = nums[:i]
            rnum = nums[i:]

            r = lnum.count(0)
            l = rnum.count(1)
            score = r + l
            print(lnum,rnum,score)
            scores[i] = score
        a = sorted(scores.items(), key = lambda x : x[1],reverse=True)
        
        ctr = 0
        final = []
    
        for i in a:
            if ctr == 0:
                if final == []: 
                    final.append(i[0])
                    maxnum = i[1]
                    ctr += 1
            elif maxnum == i[1]:
                final.append(i[0])
            ctr +=1
        return final

print(maxScoreIndices([0,0,0,1,1,0,1,0,1]))