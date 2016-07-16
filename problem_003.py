# Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        i = 0
        j = 0
        w = {}
        while j < len(s):
            x = self.getCode(s[j])
            # print j, s[j]
            if x not in w:
                w[x] = -1
            if w[x] >= 0:
                res = max(res, j - i)
                ix = i
                i = w[x] + 1
                for k in xrange(ix, w[x] + 1):
                    # print "rem", k, s[k]
                    w[self.getCode(s[k])] = -1
            w[x] = j
            j += 1
        res = max(res, j - i)
        return res
        
    def getCode(self, c):
        return ord(c)-97