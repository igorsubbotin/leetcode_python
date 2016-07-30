# Combination Sum II - https://leetcode.com/problems/combination-sum-ii/
from copy import copy

class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        s = []
        r = set()
        res = []
        for i in xrange(len(candidates)):
            x = candidates[i]
            if x > target:
                break
            if x == target:
                t = tuple([x])
                if t not in r:
                    r.add(t)
                    res.append([x])
                continue
            s.append((x, [x], i))
        while len(s) > 0:
            sm, a, ix = s.pop()
            for j in xrange(ix + 1, len(candidates)):
                x = candidates[j]
                n = sm + x
                if n > target:
                    break
                c = copy(a)
                c.append(x)
                if n == target:
                    t = tuple(c)
                    if t not in r:
                        r.add(t)
                        res.append(c)
                    continue
                s.append((n, c, j))
        return res