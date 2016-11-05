# Valid Palindrome - https://leetcode.com/problems/valid-palindrome/
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while i < j:
            if isNotValid(s[i]):
                i += 1
                continue
            if isNotValid(s[j]):
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
        
def isNotValid(c):
    return not (c.isalpha() or c.isdigit())