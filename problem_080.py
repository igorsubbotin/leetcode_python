# Remove Duplicates from Sorted Array II - https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        c = 0
        x = None
        while i < len(nums):
            if nums[i] != x:
                x = nums[i]
                c = 1
            else:
                c += 1
            nums[j] = nums[i]
            if c <= 2:
                j += 1
            i += 1
        return j