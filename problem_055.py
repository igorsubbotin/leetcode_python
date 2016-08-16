# Jump Game - https://leetcode.com/problems/jump-game/
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(nums) - 1:
            mx = 0
            ix = i
            for j in xrange(i + 1, min(len(nums), i + nums[i] + 1)):
                p = j + nums[j]
                if p > mx:
                    mx = p
                    ix = j
            if i == ix:
                return False
            i = ix
        return True