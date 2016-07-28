# Combination Sum - https://leetcode.com/problems/combination-sum/
from copy import copy

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        s = []
        r = set()
        res = []
        c = []
        for x in candidates:
            if x == target:
                res.append([x])
                continue
            if x > target:
                continue
            c.append(x)
            s.append(([x], x))
        candidates = c
        while len(s) > 0:
            a, n = s.pop()
            for x in candidates:
                nn = n + x
                if nn > target:
                    continue
                c = copy(a)
                c.append(x)
                if nn == target:
                    t = tuple(c)
                    if t not in r:
                        r.add(t)
                        res.append(t)
                    continue
                s.append((c, nn))
        return res