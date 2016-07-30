# First Missing Positive - https://leetcode.com/problems/first-missing-positive/
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 1
        for i in xrange(len(nums)):
            move(nums, nums[i], i)
        if nums[0] != 1:
            return 1
        prev = 1
        for i in xrange(1, len(nums)):
            n = nums[i]
            if n - prev != 1:
                return i + 1
            prev = n
        return nums[len(nums) - 1] + 1

def move(a, n, i):
    if n <= 0:
        return
    ix = n - 1
    if ix == i:
        return
    if ix >= len(a):
        return
    t = a[ix]
    a[ix] = n
    move(a, t, ix)