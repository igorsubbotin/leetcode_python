# Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums.sort()
        a = nums[0]
        i = 1
        j = 1
        while i < len(nums):
            if nums[i] != a:
                a = nums[i]
                nums[j] = a
                j += 1
            i += 1
        return j