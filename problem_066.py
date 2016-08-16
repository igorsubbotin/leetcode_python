# Plus One - https://leetcode.com/problems/plus-one/
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        shift = 1
        for i in reversed(xrange(len(digits))):
            if shift == 0:
                break
            v = digits[i] + shift
            shift = v / 10
            digits[i] = v % 10
        if shift > 0:
            digits = [shift] + digits
        return digits