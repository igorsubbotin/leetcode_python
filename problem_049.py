# Group Anagrams - https://leetcode.com/problems/anagrams/
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for x in strs:
            a = list(x)
            a.sort()
            t = tuple(a)
            if t not in d:
                d[t] = []
            d[t].append(x)
        res = []
        i = 0
        for key in d:
            res.append([])
            for x in d[key]:
                res[i].append(x)
            i += 1
        return res