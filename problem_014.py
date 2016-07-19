# Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/
import sys

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        mn = sys.maxint
        for s in strs:
            if len(s) < mn:
                mn = len(s)
        res = ""
        stop = False
        for i in xrange(mn):
            c = strs[0][i]
            for j in xrange(1, len(strs)):
                if strs[j][i] != c:
                    stop = True
                    break
            if stop:
                break
            else:
                res += c
        return res