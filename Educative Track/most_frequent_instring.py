class Solution:
    def mostFrequent(self, l: List[int], key: int) -> int:
        d={}
        for i in range(len(l)-1):
            if l[i]==key:
                if l[i+1] in d:
                    d[l[i+1]]=d[l[i+1]]+1
                else:
                    d[l[i+1]]=1
        most=0
        for key in d:
            if d[key]>most:
                most=d[key] 
                value=key
                
        return value