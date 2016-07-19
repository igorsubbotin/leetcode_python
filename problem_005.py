# Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        mx = 0
        for i in xrange(len(s)):
            for j in [0, 1]:
                l, left, right = self.findLongestPalindrome(s, i - j, i + 1)
                if l > mx:
                    mx = l
                    mx_left = left
                    mx_right = right
        return s[mx_left:mx_right+1]
        
    def findLongestPalindrome(self, s, left, right):
        while True:
            if left < 0 or right == len(s) or s[left] != s[right]:
                left += 1
                right -= 1
                break
            left -= 1
            right += 1
        l = right - left + 1
        return [l, left, right]