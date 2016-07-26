# Next Permutation - https://leetcode.com/problems/next-permutation/
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        inv = findFirstInversion(nums)
        if inv is None:
            quicksort(nums)
            return
        print inv
        i, j = inv
        t = nums[j]
        nums[j] = nums[i]
        nums[i] = t
        quicksort(nums, i + 1)
        print nums
        
        
def findFirstInversion(a):
    mx = -1
    mx_ix = None
    for i in reversed(xrange(len(a))):
        item = a[i]
        for j in reversed(xrange(i)):
            if a[j] < item and j > mx:
                mx = j
                mx_ix = [j, i]
    return mx_ix
    
def partition(array, begin, end):
    pivot = begin
    for i in xrange(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot
    
    
def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    if begin >= end:
        return
    pivot = partition(array, begin, end)
    quicksort(array, begin, pivot-1)
    quicksort(array, pivot+1, end)