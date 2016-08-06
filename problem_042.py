# Trapping Rain Water - https://leetcode.com/problems/trapping-rain-water/
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0
        res = 0
        i = 0
        j = len(height) - 1
        prev = 0
        while True:
            if height[i] < height[j]: 
                while i <= j and height[i] <= prev:
                    res -= height[i]
                    i += 1
            else:
                while i <= j and height[j] <= prev:
                    res -= height[j]
                    j -= 1
            if i > j:
                break
            mn = min(height[i], height[j])
            res += (mn - prev) * (j - i + 1)
            prev = mn
        return res