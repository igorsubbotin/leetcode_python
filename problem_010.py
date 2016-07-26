# Regular Expression Matching - https://leetcode.com/problems/regular-expression-matching/
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        p += chr(0)
        s += chr(0)
        i = 0
        pattern = []
        while i < len(p):
            item, shift = self.getPatternItem(p, i)
            pattern.append(item)
            i += shift
        pattern = self.packPattern(pattern)
        q = []
        q.append((0, 0, s[0], pattern[0]))
        counter = 0
        while len(q) > 0:
            i, j, c, item = q.pop()
            pc, star = item
            hit = pc == "." or pc == c
            if not star and not hit:
                continue
            if hit and i == len(s) - 1 and j == len(pattern) - 1:
                return True
            if star:
                if hit:
                    if i + 1 != len(s) and j + 1 != len(pattern):
                        q.append((i + 1, j + 1, s[i + 1], pattern[j + 1]))
                    if i + 1 != len(s):
                        q.append((i + 1, j, s[i + 1], pattern[j]))
                if j + 1 != len(pattern):
                    q.append((i, j + 1, c, pattern[j + 1]))
            else:
                if i + 1 != len(s) and j + 1 != len(pattern):
                    q.append((i + 1, j + 1, s[i + 1], pattern[j + 1]))
        return False
        
    def getPatternItem(self, p, i):
        j = i + 1
        star = False
        if j < len(p) and p[j] == "*":
            star = True
        shift = 1
        if star:
            shift = 2
        return [(p[i], star), shift]
        
    def packPattern(self, pattern):
        prev = ("", False)
        res = []
        for item in pattern:
            if item == prev and item[1]:
                continue
            prev = item
            res.append(item)
        return res