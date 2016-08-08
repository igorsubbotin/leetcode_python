# Merge Intervals - https://leetcode.com/problems/merge-intervals/

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        res = []
        intervals = sorted(intervals, key = lambda x: x.start)
        current = Interval(intervals[0].start, intervals[0].end)
        for i in xrange(1, len(intervals)):
            interval = intervals[i]
            if current.end < interval.start:
                res.append(current)
                current = Interval(interval.start, interval.end)
            else:
                current.end = max(current.end, interval.end)
        res.append(current)
        return res