# Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/
import sys

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        p = self.findBestCut(nums1, nums2) + self.findBestCut(nums2, nums1)
        mn = sys.maxint
        res = []
        for diff, n in p:
            if diff < mn:
                mn = diff
                res = []
            if diff == mn:
                res.append(n)
        return float(sum(res)) / len(res)
        
    def findBestCut(self, a, b):
        if len(a) == 0:
            return []
        v = set()
        mn = sys.maxint
        res = []
        start = 0
        end = len(a) - 1
        i = len(a) / 2
        while True:
            if i in v:
                break
            v.add(i)
            l, r = self.findCut(b, a[i])
            left = i + l
            right = len(a) - i - 1 + r
            diff = abs(right - left)
            if diff < mn:
                mn = diff
                res = []
            if diff == mn:
                res.append((diff, a[i]))
            if right > left:
                start = i
                i = start + (end - start) / 2
                if end - start == 1:
                    i += 1
            elif right < left:
                end = i
                i = start + (end - start) / 2
            else:
                return [(0, a[i])]
        return res
        
    def findCut(self, a, n):
        return self.findCutRecursive(a, n, 0, len(a) - 1)
        
    def findCutRecursive(self, a, n, left, right):
        if len(a) == 0:
            return (0, 0)
        ln = right - left + 1
        median = left + ln / 2
        if ln == 1:
            if n < a[left]:
                return (left, len(a) - left)
            elif n > a[left]:
                return (left + 1, len(a) - left - 1)
            else:
                return (left, len(a) - left - 1)
        if ln == 2:
            if n < a[left]:
                return (left, len(a) - left)
            elif n == a[left]:
                return (left, len(a) - left - 1)
            elif n > a[left] and n < a[right]:
                return (right, len(a) - right)
            elif n == a[right]:
                return (right, len(a) - right - 1)
            elif n > a[right]:
                return (right + 1, len(a) - right - 1)
        if n < a[median]:
            return self.findCutRecursive(a, n, left, median)
        elif n > a[median]:
            return self.findCutRecursive(a, n, median, right)
        else:
            return (median, len(a) - median - 1)