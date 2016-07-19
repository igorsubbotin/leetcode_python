# Integer to Roman - https://leetcode.com/problems/integer-to-roman/
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        a = [0] * 4
        i = 0
        while num > 0:
            a[i] = num % 10
            num /= 10 
            i += 1
        return "M" * a[3] + self.getUnderThousand(a[2]) + self.getUnderHundred(a[1]) + self.getUnderTen(a[0])
        
    def getUnderTen(self, n):
        return self.getRoman(n, "I", "V", "X")
        
    def getUnderHundred(self, n):
        return self.getRoman(n, "X", "L", "C")
        
    def getUnderThousand(self, n):
        return self.getRoman(n, "C", "D", "M")
        
    def getRoman(self, n, one, five, ten):
        if n == 0:
            return ""
        if n > 0 and n < 4:
            return one * n
        elif n == 4:
            return one + five
        elif n < 9:
            return five + one * (n - 5)
        elif n == 9:
            return one + ten