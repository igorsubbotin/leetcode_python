# Jump Game II - https://leetcode.com/problems/jump-game-ii/
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        i = 0
        steps = 0
        while True:
            steps += 1
            p = nums[i]
            mx = 0
            ix = 0
            for j in xrange(1, p + 1):
                if i + j == len(nums) - 1:
                    return steps
                n = nums[i + j] - p + j
                if n > mx:
                    mx = n
                    ix = i + j
            i = ix
        return steps