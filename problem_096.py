# Unique Binary Search Trees - https://leetcode.com/problems/unique-binary-search-trees/
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return getNumTrees(n)
        
cache = {}
def getNumTrees(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    if n not in cache:
        res = 0
        for i in xrange(n):
            res += getNumTrees(n - i - 1) * getNumTrees(i)
        cache[n] = res
    return cache[n]