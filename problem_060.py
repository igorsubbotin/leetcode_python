# Permutation Sequence - https://leetcode.com/problems/permutation-sequence/
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        return permutate(range(1, n + 1), k)
       
def permutate(a, k):
    n = len(a)
    if n == 1:
        return str(a[0])
    c = factorial(n - 1)
    ix = (k - 1) / c
    return str(a[ix]) + permutate(a[:ix] + a[ix + 1:], k - ix * c)
    
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)