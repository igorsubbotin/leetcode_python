# Search Insert Position - https://leetcode.com/problems/search-insert-position/
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.searchIndex(nums, 0, len(nums) - 1, target)
        
    def searchIndex(self, a, left, right, target):
        ln = right - left + 1
        median = left + ln / 2
        if ln == 1:
            if target <= a[median]:
                return left
            else:
                return left + 1
        if ln == 2:
            if target <= a[left]:
                return left
            elif target > a[left] and target <= a[right]:
                return right
            else:
                return right + 1
        if target < a[median]:
            return self.searchIndex(a, left, median, target)
        elif target > a[median]:
            return self.searchIndex(a, median, right, target)
        else:
            return median