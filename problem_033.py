# Search in Rotated Sorted Array - https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        shift = (findMaxIndex(nums) + 1) % len(nums)
        ix = findIndex(nums, target, shift)
        if ix == -1:
            return -1
        return getIndex(nums, ix, shift)
        
def findIndex(a, n, shift):
    return findIndexRecursively(a, n, shift, 0, len(a) - 1)
    
def findIndexRecursively(a, n, shift, left, right):
    left_shift = getIndex(a, left, shift)
    right_shift = getIndex(a, right, shift)
    ln = right - left + 1
    if ln < 3:
        if a[left_shift] == n:
            return left
        elif a[right_shift] == n:
            return right
        else:
            return -1
    median = left + ln / 2
    median_shift = getIndex(a, median, shift)
    if n > a[median_shift]:
        return findIndexRecursively(a, n, shift, median + 1, right)
    elif n < a[median_shift]:
        return findIndexRecursively(a, n, shift, left, median - 1)
    else:
        return median

def getIndex(a, ix, shift):
    return (ix + shift) % len(a) 
        
def findMaxIndex(a):
    return findMaxIndexRecursively(a, 0, len(a) - 1)

def findMaxIndexRecursively(a, left, right):
    ln = right - left + 1
    median = left + ln / 2
    if ln < 3:
        if a[left] > a[right]:
            return left
        else:
            return right
    if a[median] < a[left]:
        return findMaxIndexRecursively(a, left, median)
    else:
        return findMaxIndexRecursively(a, median, right)