# Multiply Strings - https://leetcode.com/problems/multiply-strings/
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return numberToString(multiply(parseNumber(num1), parseNumber(num2)))
    
def multiply(num1, num2):
    return num1 * num2

def parseNumber(s):
    res = 0
    for i in xrange(len(s)):
        res += parseDigit(s[len(s) - i- 1]) * 10 ** i
    return res
        
def parseDigit(c):
    return ord(c)-48
    
def numberToString(n):
    if n == 0:
        return "0"
    res = ""
    while n > 0:
        res = chr(n % 10 + 48) + res
        n /= 10
    return res