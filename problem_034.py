# Search for a Range - https://leetcode.com/problems/search-for-a-range/
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ix = findIndex(nums, target)
        if ix == -1:
            return [-1, -1]
        start = ix
        while start >= 0 and nums[start] == target:
            start -= 1
        end = ix
        while end < len(nums) and nums[end] == target:
            end += 1
        return [start + 1, end - 1]
        
def findIndex(a, n):
    return findIndexRecursive(a, n, 0, len(a) - 1)

def findIndexRecursive(a, n, left, right):
    ln = right - left + 1
    median = left + ln / 2
    if ln == 1:
        if a[left] == n:
            return left
        else:
            return -1
    if ln == 2:
        if a[left] == n:
            return left
        elif a[right] == n:
            return right
        else:
            return -1
    
    if n < a[median]:
        return findIndexRecursive(a, n, left, median)
    if n > a[median]:
        return findIndexRecursive(a, n, median, right)
    return median