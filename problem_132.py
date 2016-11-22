# Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        return getCuts(s)
        
cache = {}
def getCuts(s):
    if s not in cache:
        n = len(s)
        if isPalindrome(s):
            cache[s] = 0
            return cache[s]
        res = n - 1
        for i in xrange(1, n):
            if isPalindrome(s[:i]) and isPalindrome(s[i:]):
                cache[s] = 1
                return cache[s]
        for i in xrange(1, n):
            b = s[:i]
            if isPalindrome(b):
                cuts = getCuts(s[i:]) + 1
                res = min(res, cuts)
                if res == 1:
                    break
        cache[s] = res
    return cache[s]
        
def isPalindrome(s):
    n = len(s)
    for i in xrange(n / 2):
        if s[i] != s[n-i-1]:
            return False
    return True