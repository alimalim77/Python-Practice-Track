class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        case1, case2 , case3 = True, True, True
        
        if word.isupper():
            return case1
        elif word.islower():
            return case2
        elif word.istitle():
            return case3
        else:
            return False