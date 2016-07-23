# Implement strStr() - https://leetcode.com/problems/implement-strstr/
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        i = 0
        j = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                j += 1
            else:
                i -= j
                j = 0
            i += 1
        if j != len(needle):
            return -1
        return i - j