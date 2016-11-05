# Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 0
        mn = sys.maxint
        mx = 0
        for i in xrange(len(prices)):
            v = prices[i]
            if v < mn:
                mx = 0
                mn = v
            mx = max(mx, v)
            res = max(res, mx - mn)
        return res