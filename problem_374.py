# 374. Guess Number Higher or Lower - https://leetcode.com/problems/guess-number-higher-or-lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.findNumber(1, n)
        
    def findNumber(self, left, right):
        length = right - left + 1;
        median = left + length / 2;
        if length < 3:
            if guess(left) == 0:
                return left
            if guess(right) == 0:
                return right
            return
        medianGuess = guess(median);
        if medianGuess == -1:
            return self.findNumber(left, median - 1)
        elif medianGuess == 1:
            return self.findNumber(median + 1, right)
        return median