# Remove Element - https://leetcode.com/problems/remove-element/
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = 0
        for i in reversed(range(len(nums))):
            if nums[i] == val:
                l += 1
                for j in xrange(i + 1, len(nums)):
                    self.swap(nums, j - 1, j)
        return len(nums) - l
                    
    def swap(self, a, i, j):
        t = a[i]
        a[i] = a[j]
        a[j] = t