# Reverse Words in a String - https://leetcode.com/problems/reverse-words-in-a-string/
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        words.reverse()
        return " ".join(x for x in words)