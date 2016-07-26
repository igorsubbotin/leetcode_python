# Next Permutation - https://leetcode.com/problems/next-permutation/
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ix = -1
        for i in reversed(xrange(len(nums) - 1)):
            if nums[i] < nums[i + 1]:
                ix = i
                break
        if ix != -1:
            for i in xrange(ix + 1, len(nums)):
                if nums[i] <= nums[ix]:
                    i -= 1
                    break
            swap(nums, i, ix)
        for i in xrange((len(nums) - 1 - ix) / 2):
            swap(nums, ix + i + 1, len(nums) - i - 1)
        
def swap(a, i, j):
    t = a[i]
    a[i] = a[j]
    a[j] = t