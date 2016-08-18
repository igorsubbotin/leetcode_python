# Combinations - https://leetcode.com/problems/combinations/
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return combineRecursive(range(1, n + 1), k)
        
def combineRecursive(a, k, ix = 0):
    if k == 1:
        return [[a[i]] for i in xrange(ix, len(a))]
    res = []
    for i in xrange(ix, len(a)):
        l = combineRecursive(a, k - 1, i + 1)
        if len(l) == 0:
            break
        for j in l:
            j.append(a[i])
            res.append(j)
    return res