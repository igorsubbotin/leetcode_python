# Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n < 2:
            return 0
        forward = [0] * n
        backward = [0] * n
        mn = prices[0]
        for i in range(1, len(prices)):
            forward[i] = max(forward[i-1], prices[i]-mn)
            mn = min(mn, prices[i])
        mx = prices[-1]
        for i in range(len(prices)-2,-1,-1):
            backward[i] = max(backward[i+1], mx - prices[i])
            mx = max(mx, prices[i])
        profits = [i+j for i, j in zip(forward, backward)]
        return max(profits)