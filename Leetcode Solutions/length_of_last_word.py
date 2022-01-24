class Solution(object):
    def lengthOfLastWord(self, s):
        """
        #58
        :type s: str
        :rtype: int
        """
        strlist = []
        i=0
        while i < len(s):
            lenstr = ""
            while i < len(s)  and s[i].isalpha():
                lenstr = lenstr + s[i]
                i = i+1
            if len(lenstr) != 0:
                strlist.append(lenstr)
            i= i+1
        return len(strlist[-1])
        