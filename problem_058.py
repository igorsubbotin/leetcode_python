# Length of Last Word - https://leetcode.com/problems/length-of-last-word/
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for c in s[::-1]:
            if c == ' ':
                if res > 0:
                    break
            else:
                res += 1
        return res