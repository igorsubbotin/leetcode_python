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
        for diff, ix in p:
            diff = abs(diff)
            if ix is None:
                continue
            if diff < mn:
                mn = diff
                res = []
            if diff == mn:
                res.append(ix)
        return float(sum(res)) / len(res)
        
    def findBestCut(self, a, b):
        if len(a) == 0:
            return [(sys.maxint, None), (sys.maxint, None)]
        v = set()
        mn_plus = sys.maxint
        mn_plus_i = None
        mn_minus = -sys.maxint
        mn_minus_i = None
        start = 0
        end = len(a) - 1
        i = len(a) / 2
        while True:
            if i in v:
                break
            v.add(i)
            n = a[i]
            l, r = self.findCut(b, n)
            left = i + l
            right = len(a) - i - 1 + r
            diff = right - left
            if diff > 0:
                if diff < mn_plus:
                    mn_plus = diff
                    mn_plus_i = i
                start = i
                i = start + (end - start) / 2
                if end - start == 1:
                    i += 1
            elif diff < 0:
                if diff > mn_minus:
                    mn_minus = diff
                    mn_minus_i = i
                end = i
                i = start + (end - start) / 2
            else:
                return [(0, a[i]), (0, a[i])]
        minus_res = None
        if mn_minus_i is not None:
            minus_res = a[mn_minus_i]
        plus_res = None
        if mn_plus_i is not None:
            plus_res = a[mn_plus_i]
        return [(mn_minus, minus_res), (mn_plus, plus_res)]
        
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