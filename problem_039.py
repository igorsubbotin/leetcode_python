# Combination Sum - https://leetcode.com/problems/combination-sum/
from copy import copy

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        s = []
        res = []
        c = []
        ix = 0
        for i in xrange(len(candidates)):
            x = candidates[i]
            if x == target:
                res.append([x])
                continue
            if x > target:
                break
            c.append(x)
            s.append(([x], x, ix))
            ix += 1
        candidates = c
        while len(s) > 0:
            a, n, i = s.pop()
            for j in xrange(i, len(candidates)):
                x = candidates[j]
                nn = n + x
                if nn > target:
                    break
                c = copy(a)
                c.append(x)
                if nn == target:
                    res.append(c)
                    continue
                s.append((c, nn, j))
        return res