# Regular Expression Matching - https://leetcode.com/problems/regular-expression-matching/
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.cache = {}
        s += chr(0)
        p += chr(0)
        return self.isMatchRecursively(s, p, 0, 0)

    def isMatchRecursively(self, s, p, i, j):
        key = (i, j)
        if key in self.cache:
            return self.cache[key]
        if p[j] == chr(0):
            v = s[i] == chr(0)
            self.cache[key] = v
            return v
        if p[j + 1] != "*":
            v = ((p[j] == s[i]) or (p[j] == "." and s[i] != chr(0))) and self.isMatchRecursively(s, p, i + 1, j + 1)
            self.cache[key] = v
            return v
        while (p[j] == s[i]) or (p[j] == "." and s[i] != chr(0)):
            if self.isMatchRecursively(s, p, i, j + 2):
                v = True
                self.cache[key] = v
                return v
            i += 1
        v = self.isMatchRecursively(s, p, i, j + 2)
        self.cache[key] = v
        return v