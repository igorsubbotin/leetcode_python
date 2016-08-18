# Sort Colors - https://leetcode.com/problems/sort-colors/
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return
        i = 0
        j = n - 1
        while i < len(nums) and nums[i] == 0:
            i += 1
        if i == len(nums):
            return
        ix = i + 1
        t = nums[ix - 1]
        nums[ix - 1] = 1
        while ix <= j + 1:
            if t == 0:
                t = nums[i]
                nums[i] = 0
                i += 1
            elif t == 1:
                if ix == j + 1:
                    break
                t = nums[ix]
                nums[ix] = 1
                ix += 1
            elif t == 2:
                t = nums[j]
                nums[j] = 2
                j -= 1