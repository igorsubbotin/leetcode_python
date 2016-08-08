# Insert Interval - https://leetcode.com/problems/insert-interval/

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)
        intervals = sorted(intervals, key = lambda x: x.start)
        res = []
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