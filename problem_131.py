# Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        return getPalindromes(s)
        
cache = {}
def getPalindromes(s):
    if s not in cache:
        n = len(s)
        res = []
        for i in xrange(1, n):
            b = s[:i]
            if isPalindrome(b):
                for x in getPalindromes(s[i:]):
                    res.append([b] + x)
        if isPalindrome(s):
            res.append([s])
        cache[s] = res
    return cache[s]
     
pcache = {}
def isPalindrome(s):
    if s not in pcache:
        pcache[s] = True
        n = len(s)
        for i in xrange(n / 2):
            if s[i] != s[n-i-1]:
                pcache[s] = False
                break
    return pcache[s]