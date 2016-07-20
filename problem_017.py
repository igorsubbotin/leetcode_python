# Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        a = [""]
        for d in digits:
            b = []
            for l in self.getLetters(d):
                for x in a:
                    b.append(x + l)
            a = b
        return a
                
    def getLetters(self, n):
        n = int(n)
        if n == 2:
            return "abc"
        if n == 3:
            return "def"
        if n == 4:
            return "ghi"
        if n == 5:
            return "jkl"
        if n == 6:
            return "mno"
        if n == 7:
            return "pqrs"
        if n == 8:
            return "tuv"
        if n == 9:
            return "wxyz"
        return ""